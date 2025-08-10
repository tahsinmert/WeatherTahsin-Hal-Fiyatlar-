# 🌤️ WeatherTahsin Hal Fiyatları - Ultra Detaylı Elma Piyasası Takip Sistemi

## 📋 Proje Hakkında

Bu proje, Türkiye'deki hal fiyatlarını çoklu kaynaklardan toplayarak ultra detaylı elma fiyat analizi sunan bir web uygulamasıdır. Tahsin Mert Mutlu tarafından geliştirilmiştir.

## 🚀 Özellikler

### 📊 Veri Kaynakları
- **İBB (İstanbul Büyükşehir Belediyesi)**: https://tarim.ibb.istanbul/avrupa-yakasi-hal-mudurlugu/hal-fiyatlari.html
- **Başak App**: https://basakapp.com/hal-borsa-fiyatlari
- **TOBB (Türkiye Odalar ve Borsalar Birliği)**: https://borsa.tobb.org.tr/
- **TMO (Toprak Mahsulleri Ofisi)**: https://www.tmo.gov.tr/

### 🍎 Elma Çeşitleri
- Elma (Gransimit) - 1. Sınıf
- Elma (Golden) - 1. Sınıf
- Elma (Starkin) - 1. Sınıf
- Elma(gransimit)II. - 2. Sınıf
- Elma(GoldenII.) - 2. Sınıf
- Elma(starkin)II. - 2. Sınıf
- Elma (Organik Gransimit) - Organik
- Elma (Pink Lady) - 1. Sınıf

### 📱 Mobil Uyumluluk
- Responsive tasarım
- Mobil kartlar
- Dokunmatik etkileşim
- Otomatik veri güncelleme

### 🔄 Otomatik Güncelleme
- Sayfa girişinde otomatik yenileme
- Sekme değişiminde güncelleme
- 5 dakikada bir otomatik yenileme
- Manuel yenileme butonu

## 🛠️ Kurulum

### Gereksinimler
```bash
pip install -r requirements.txt
```

### Çalıştırma
```bash
python3 server.py
```

### Erişim
- Web Sayfası: http://localhost:5000
- API Endpoint: http://localhost:5000/ultra_detayli_elma_fiyatlari.json

## 📁 Dosya Yapısı

```
WeatherTahsin_Hal_Fiyatlari_Projesi/
├── hal_fiyatlari_scraper.py      # Ana web scraping modülü
├── server.py                     # Flask web sunucusu
├── index.html                    # Ana web sayfası
├── templates/
│   └── index.html               # Template dosyası
├── ultra_detayli_elma_fiyatlari.json  # Veri dosyası
├── requirements.txt              # Python bağımlılıkları
├── README.md                     # Bu dosya
└── README_IBB.md                # Detaylı dokümantasyon
```

## 🔌 API Endpoints

### Ana Endpoints
- `GET /` - Ana web sayfası
- `GET /ultra_detayli_elma_fiyatlari.json` - Ultra detaylı veri
- `GET /ibb_elma_fiyatlari.json` - Eski format (geriye uyumluluk)

### API Endpoints
- `GET /api/statistics` - İstatistikler
- `GET /api/sources` - Veri kaynakları
- `GET /api/products` - Ürün listesi
- `GET /api/refresh` - Veri yenileme
- `GET /health` - Sistem durumu

## 📊 Veri Yapısı

### Ultra Detaylı Veri Formatı
```json
{
  "metadata": {
    "scraper_version": "2.0.0",
    "data_collection_time": "2025-08-10 17:30:00",
    "data_quality_level": "Ultra High"
  },
  "aggregated_data": [
    {
      "name": "Elma (Gransimit)",
      "min_price": 70.0,
      "max_price": 90.0,
      "avg_price": 80.0,
      "quality": "1. Sınıf",
      "organic_status": false,
      "price_trend": "Yükseliş",
      "price_volatility": 25.0
    }
  ],
  "statistics": {
    "price_statistics": {...},
    "quality_distribution": {...},
    "volatility_analysis": {...}
  },
  "quality_metrics": {
    "overall_quality_score": 90.3,
    "data_freshness": 95,
    "accuracy_score": 92
  }
}
```

## 🎨 Özellikler

### Görselleştirme
- Chart.js ile interaktif grafikler
- Kalite bazlı renk kodlaması
- Trend analizi görselleştirmesi
- Mobil uyumlu kartlar

### Veri Kalitesi
- Çoklu kaynak doğrulama
- Veri tazeliği metrikleri
- Tutarlılık kontrolü
- Hata yönetimi

### Kullanıcı Deneyimi
- Gerçek zamanlı güncelleme
- Bildirim sistemi
- Responsive tasarım
- Kolay navigasyon

## 🔗 Bağlantılar

- **WeatherTahsin**: https://weathertahsin.netlify.app
- **İBB Hal Fiyatları**: https://tarim.ibb.istanbul/avrupa-yakasi-hal-mudurlugu/hal-fiyatlari.html
- **Başak App**: https://basakapp.com/hal-borsa-fiyatlari

## 👨‍💻 Geliştirici

**Tahsin Mert Mutlu** tarafından kodlanmıştır.

## 📄 Lisans

Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.

## 🆘 Destek

Herhangi bir sorun veya öneri için lütfen iletişime geçin.

---

**Sistem Versiyonu**: v2.0.0  
**Son Güncelleme**: 10 Ağustos 2025  
**Veri Kalitesi**: Ultra High
