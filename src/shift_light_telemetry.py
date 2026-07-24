import pymem
import serial
import time

# --- AYARLAR ---
PORT = 'COM9'  # Aygıt Yöneticisi'nden kontrol et
BAUD_RATE = 115200

# Pointer Zinciri 
# [[[speed.exe+0x5C2520]+0x48]+0x48]+0x144
BASE_OFFSET = 0x5C2520
OFFSETS = [0x48, 0x48, 0x144]

# Haritalama Limitleri
MIN_RPM = 500
MAX_RPM = 9500
LED_COUNT =11

# --- SİSTEM BAŞLATMA ---
try:
    pm = pymem.Pymem("speed.exe")
    base_address = pm.base_address
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print("Dashboard Başarıyla Başlatıldı. LED'ler hazır!")
except Exception as e:
    print(f"HATA: Sistem başlatılamadı. Oyun açık mı ve port doğru mu? -> {e}")
    exit()

# Hareketli Ortalama (Smoothness) için tampon
rpm_buffer = []


def get_rpm():
    """Pointer zincirini takip ederek ham RPM verisini okur."""
    try:
        ptr1 = pm.read_int(base_address + BASE_OFFSET)
        ptr2 = pm.read_int(ptr1 + OFFSETS[0])
        ptr3 = pm.read_int(ptr2 + OFFSETS[1])
        rpm = pm.read_int(ptr3 + OFFSETS[2])
        return rpm
    except:
        return 0


def get_mapped_level(current_rpm):
    """500-9500 RPM aralığını 0-8 LED seviyesine haritalar."""
    # Normalizasyon
    normalized = (current_rpm - MIN_RPM) / (MAX_RPM - MIN_RPM)

    mapped = normalized * 11.8 
    # Değerleri 0 ile 8 arasında kilitler
    return int(max(0, min(mapped, LED_COUNT)))


try:
    while True:
        raw_rpm = get_rpm()

        # Hareketli Ortalama (Gürültüyü temizle)
        rpm_buffer.append(raw_rpm)
        if len(rpm_buffer) > 5: rpm_buffer.pop(0)
        smooth_rpm = sum(rpm_buffer) / len(rpm_buffer)

        # Haritalama
        level = get_mapped_level(smooth_rpm)

        # Veriyi Arduino'ya gönder
        ser.write(bytes([level]))


        time.sleep(0.02)  # 50Hz güncelleme

except KeyboardInterrupt:
    print("\nDashboard kapatılıyor...")
    ser.close()
