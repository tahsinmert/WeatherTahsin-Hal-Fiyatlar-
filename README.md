# WeatherTahsin-Hal-Fiyatları 🌤️🍎

Türkiye'deki hal fiyatlarını takip eden, özellikle elma fiyatlarına odaklanan ultra detaylı web scraping ve API projesi.

## 📋 Proje Hakkında

Bu proje, İBB (İstanbul Büyükşehir Belediyesi), Başak App, TOBB ve TMO gibi resmi kaynaklardan hal fiyatlarını çekerek, özellikle elma fiyatlarını detaylı bir şekilde analiz eden bir sistemdir. Flask tabanlı web API'si ve modern web arayüzü ile kullanıcılara güncel fiyat bilgilerini sunar.

## ✨ Özellikler

- **Çoklu Kaynak Desteği**: İBB, Başak App, TOBB, TMO kaynaklarından veri çekme
- **Ultra Detaylı Analiz**: Fiyat, kalite, bölge, sezon analizi
- **Gerçek Zamanlı Veri**: Otomatik veri güncelleme sistemi
- **Web API**: RESTful API endpoints
- **Modern Web Arayüzü**: Responsive HTML/CSS/JavaScript arayüzü
- **İstatistiksel Analiz**: Fiyat trendleri, volatilite analizi
- **Veri Kalitesi Metrikleri**: Güvenilirlik skorları ve kalite değerlendirmesi

## 🚀 Kurulum

### Gereksinimler

- Python 3.7+
- pip (Python paket yöneticisi)

### Adım Adım Kurulum

1. **Repository'yi klonlayın:**
```bash
git clone https://github.com/tahsinmert/WeatherTahsin-Hal-Fiyatlar-.git
cd WeatherTahsin-Hal-Fiyatlar-
```

2. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

3. **Uygulamayı çalıştırın:**
```bash
python server.py
```

4. **Tarayıcınızda açın:**
```
http://localhost:5000
```

## 📊 API Endpoints

### Ana Endpoints

- `GET /` - Ana web sayfası
- `GET /ibb_elma_fiyatlari.json` - Eski format uyumluluğu için elma fiyatları
- `GET /ultra_detayli_elma_fiyatlari.json` - Ultra detaylı elma fiyatları
- `GET /api/refresh` - Verileri manuel olarak yenile
- `GET /api/statistics` - Detaylı istatistikler
- `GET /api/sources` - Veri kaynakları bilgisi
- `GET /api/products` - Ürün listesi
- `GET /health` - Sistem sağlık kontrolü

### Örnek API Kullanımı

```bash
# Elma fiyatlarını al
curl http://localhost:5000/ultra_detayli_elma_fiyatlari.json

# Verileri yenile
curl http://localhost:5000/api/refresh

# İstatistikleri al
curl http://localhost:5000/api/statistics
```

## 🔧 Veri Yapısı

### Ultra Detaylı Veri Formatı

```json
{
  "metadata": {
    "scraper_version": "2.0.0",
    "data_collection_time": "2024-01-15 14:30:00",
    "data_quality_level": "Ultra High",
    "update_frequency": "Real-time"
  },
  "aggregated_data": [
    {
      "name": "Amasya Elması",
      "min_price": 8.50,
      "max_price": 12.00,
      "avg_price": 10.25,
      "unit": "TL/kg",
      "quality": "Premium",
      "market": "İBB Avrupa Yakası Hal",
      "region": "İstanbul",
      "confidence_level": 95
    }
  ],
  "statistics": {
    "total_products": 15,
    "price_range": {"min": 5.00, "max": 18.00},
    "avg_price": 11.50
  },
  "quality_metrics": {
    "data_freshness": 98,
    "completeness_score": 95,
    "accuracy_score": 92
  }
}
```

## 🛠️ Geliştirme

### Proje Yapısı

```
weather-tahsin-hal/
├── server.py                          # Flask web sunucusu
├── hal_fiyatlari_scraper.py          # Ana scraping motoru
├── index.html                         # Web arayüzü
├── ultra_detayli_elma_fiyatlari.json # Veri dosyası
├── requirements.txt                   # Python bağımlılıkları
└── README.md                          # Bu dosya
```

### Scraper Özellikleri

- **Çoklu Kaynak Desteği**: 4 farklı resmi kaynaktan veri çekme
- **Akıllı Veri Birleştirme**: Farklı kaynaklardan gelen verileri analiz ederek birleştirme
- **Kalite Kontrolü**: Veri güvenilirliği ve tutarlılık kontrolü
- **Hata Yönetimi**: Kaynak hatalarında yedek veri kullanımı
- **İstatistiksel Analiz**: Fiyat trendleri ve volatilite hesaplama

## 📈 Veri Kaynakları

1. **İBB Avrupa Yakası Hal Müdürlüğü**
   - URL: https://tarim.ibb.istanbul/avrupa-yakasi-hal-mudurlugu/hal-fiyatlari.html
   - Güncel İstanbul hal fiyatları

2. **Başak App Hal Borsa Fiyatları**
   - URL: https://basakapp.com/hal-borsa-fiyatlari
   - Ulusal hal borsa verileri

3. **TOBB Ticaret Borsaları**
   - URL: https://borsa.tobb.org.tr/fiyat_borsa.php
   - Resmi borsa fiyatları

4. **TMO Hububat Fiyatları**
   - URL: https://www.tmo.gov.tr/
   - Devlet hububat fiyatları

## 🔍 Özellikler Detayı

### Fiyat Analizi
- Minimum, maksimum ve ortalama fiyat hesaplama
- Fiyat volatilitesi analizi
- Trend analizi ve tahminleme

### Kalite Değerlendirmesi
- Ürün kalite sınıflandırması (Premium, Standard, vb.)
- Bölgesel kalite farklılıkları
- Sezonluk kalite değişimleri

### Bölgesel Analiz
- İstanbul, Ankara, İzmir, Bursa, Antalya bölgeleri
- Bölgeler arası fiyat karşılaştırması
- Ulaşım maliyeti hesaplamaları

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

**Tahsin Mert**
- GitHub: [@tahsinmert](https://github.com/tahsinmert)
- Proje: WeatherTahsin-Hal-Fiyatları

## 📞 İletişim

Sorularınız veya önerileriniz için:
- GitHub Issues: [Proje Issues Sayfası](https://github.com/tahsinmert/WeatherTahsin-Hal-Fiyatlar-/issues)

## 🔄 Güncellemeler

### v2.0.0
- Ultra detaylı veri analizi eklendi
- Çoklu kaynak desteği genişletildi
- Web arayüzü iyileştirildi
- API endpoints eklendi

### v1.0.0
- Temel scraping özellikleri
- İBB veri kaynağı desteği
- Basit web arayüzü

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
