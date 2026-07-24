🏎️ Real-Time Game Telemetry Shift Light Indicator
English |Türkçe
English Description
A hardware-software integration project that reads real-time telemetry (RPM/Gear) data from racing games (e.g., Need for Speed) and drives an external LED array via Arduino Nano as a physical shift light indicator.
📌 Features
Real-Time Telemetry Processing: Reads live in-game engine RPM data with minimal latency.
Serial Communication: Transmits RPM states to Arduino via high-speed Serial interface.
Hardware Feedback: Sequential LED lighting sequence (Green -> Yellow -> Red) indicating optimal gear shift points.


🧠 Reverse Engineering & Memory Pointer Discovery
To extract the real-time RPM data without official game SDK support:
Memory Scanning (Cheat Engine): Monitored game process memory addresses by altering engine RPM levels in-game to isolate the exact dynamic address storing the current RPM value.
Pointer Path Analysis: Performed a pointer scan to locate the static base address and multi-level offset paths (Base Address + Offsets), ensuring the Python script reliably locates the RPM value across game restarts.
Data Extraction (Python): Utilized Win32 API / pymem libraries to hook into the process, resolve the pointer chain, and stream the float/integer RPM value in real-time.

🛠️ Hardware RequirementsMicrocontroller: 
Arduino Nano
LEDs:
 4x Green LEDs (Low RPM) 
 4x Yellow LEDs (Mid RPM) 
 3 x Red LEDs (High RPM / Redline)
Resistors: 220Ω Resistors for each LED channel
Breadboard & Jumper WiresGame 
Controller: DualShock 4 / Xbox Controller

🇹🇷 Türkçe Açıklama
Yarış oyunlarından (Örn: Need for Speed) anlık telemetri (Devir/Vites) verilerini okuyarak, Arduino Nano üzerinden harici bir LED dizilimini gerçek zamanlı bir devir ışığı (Shift Light) olarak süren donanım-yazılım entegrasyon projesi.

📌 Özellikler
Gerçek Zamanlı Telemetri İşleme: Oyun içi motor devir (RPM) verisini minimum gecikmeyle okur.
Seri İletişim: Devir durumlarını yüksek hızlı Seri Port (Serial) arayüzü üzerinden Arduino'ya aktarır.
Fiziksel Geri Bildirim: İdeal vites değiştirme noktalarını gösteren kademeli LED dizilimi (Yeşil -> Sarı -> Kırmızı).

🧠 Tersine Mühendislik ve Bellek (Pointer) Analizi
Resmi SDK desteği olmayan oyundan anlık devir verisini çekmek için izlenen adımlar:
Bellek Taraması (Cheat Engine): Oyun işlemi (process) çalışırken araç devri değiştirilerek bellek üzerindeki anlık RPM değerini tutan dinamik adres tespit edildi.
Pointer Yolu (Pointer Scan): Oyun her yeniden başladığında adresin değişmesini engellemek adına Pointer Scan ile statik ana adres (Base Address) ve ofset zinciri (Offsets) çıkarıldı.
Veri Okuma (Python): pymem / Win32 API kullanarak oyun işlemine bağlanıldı, pointer zinciri çözümlenerek anlık float/integer RPM verisi sürekli akış halinde okundu.

🛠️ Donanım Gereksinimleri
Mikrodenetleyici: Arduino Nano
LED'ler:
 4x Yeşil LED (Düşük Devir)
 4x Sarı LED (Orta Devir)
 3x Kırmızı LED (Yüksek Devir / Redline)
Dirençler: Her LED kanalı için 220Ω Direnç
Breadboard & Jumper Kablolar
Oyun Kolu: DualShock 4 / Xbox Controller🔌
 👨‍💻 Author / Yazar
 Serkan Beştaş 
 Electrical-Electronics Engineering Student | Bandırma Onyedi Eylül University 
 Feel free to star ⭐️ this repository if you found it interesting!
