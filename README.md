Güvenli Otomotiv OTA & Boot Doğrulama Simülasyonu
📌 Genel Bakış

Bu proje, bir otomotiv ECU’su için güvenli bir Over-The-Air (OTA) firmware güncelleme sistemini simüle eder.

Sistem, modern araçların firmware güncellemelerini güvenli bir şekilde indirip doğruladığını ve kurduğunu, aynı zamanda siber saldırılara karşı nasıl korunduğunu gösterir.


🚀 Özellikler
OTA firmware güncelleme simülasyonu
RSA dijital imza doğrulama
Sürüm düşürme (anti-downgrade) koruması
Secure Boot simülasyonu (SHA-256 hash doğrulama)
Firmware bütünlüğü (manipülasyon) tespiti

🏗️ Mimari
🔹 Sunucu
Firmware barındırır
Versiyon bilgisi sağlar
Firmware’i dijital olarak imzalar
🔹 ECU İstemcisi
Güncel versiyonu kontrol eder
Firmware indirir
Dijital imzayı doğrular
Sürüm düşürme saldırılarını engeller
Açılış sırasında firmware bütünlüğünü doğrular

🛠️ Kullanılan Teknolojiler
Python
FastAPI
RSA Kriptografi
SHA-256 Hashleme
REST API

🔒 Uygulanan Güvenlik Mekanizmaları
Dijital imza doğrulama
Firmware bütünlük kontrolü
Anti-downgrade mekanizması
Secure Boot doğrulaması

🎯 Amaç

Bu proje, aşağıdaki otomotiv siber güvenlik konularına hakimiyeti göstermeyi amaçlar:

OTA güncelleme güvenliği
Firmware doğrulama
Secure Boot mekanizmaları
