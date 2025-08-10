# 🚀 WeatherTahsin Hal Fiyatları - Netlify Deployment

## 📋 Proje Hakkında

Bu proje, Türkiye'deki hal fiyatlarını takip eden ultra detaylı bir web uygulamasıdır. Çoklu veri kaynaklarından elma fiyatlarını toplar ve kullanıcı dostu bir arayüzle sunar.

## 🌟 Özellikler

- **Ultra Detaylı Veri**: 8 farklı elma çeşidi
- **Çoklu Veri Kaynağı**: İBB, Başak App, TOBB, TMO
- **Mobil Uyumlu**: Responsive tasarım
- **Gerçek Zamanlı Güncelleme**: Otomatik veri yenileme
- **Gelişmiş Analiz**: Fiyat trendleri, volatilite analizi
- **Veri Kalitesi Metrikleri**: Kalite skorları ve güvenilirlik

## 🛠️ Teknolojiler

- **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript
- **Backend**: Python Flask (Netlify Functions)
- **Veri İşleme**: BeautifulSoup4, Requests
- **Görselleştirme**: Chart.js
- **Deployment**: Netlify

## 📁 Dosya Yapısı

```
├── index.html                 # Ana web sayfası
├── functions/
│   └── api.py                # Netlify Functions API
├── requirements.txt           # Python bağımlılıkları
├── runtime.txt               # Python versiyonu
├── netlify.toml             # Netlify konfigürasyonu
├── README_NETLIFY.md        # Bu dosya
└── README_IBB.md            # Detaylı dokümantasyon
```

## 🚀 Netlify'da Deploy Etme

### 1. GitHub'a Yükleme

```bash
# Projeyi GitHub'a push edin
git add .
git commit -m "Netlify deployment için hazırlandı"
git push origin main
```

### 2. Netlify'da Deploy

1. [Netlify](https://netlify.com) hesabınıza giriş yapın
2. "New site from Git" butonuna tıklayın
3. GitHub'ı seçin ve repository'nizi seçin
4. Build ayarları:
   - **Build command**: `pip install -r requirements.txt`
   - **Publish directory**: `.`
5. "Deploy site" butonuna tıklayın

### 3. Environment Variables (Opsiyonel)

Netlify dashboard'da şu environment variable'ları ekleyebilirsiniz:

```
PYTHON_VERSION=3.11.7
```

## 🔧 API Endpoints

Netlify Functions üzerinden çalışan API endpoint'leri:

- `/.netlify/functions/api/ultra_detayli_elma_fiyatlari` - Ana veri
- `/.netlify/functions/api/statistics` - İstatistikler
- `/.netlify/functions/api/products` - Ürün listesi
- `/.netlify/functions/api/health` - Sağlık kontrolü
- `/.netlify/functions/api/refresh` - Veri yenileme

## 📱 Mobil Özellikler

- **Responsive Tasarım**: Tüm ekran boyutlarında uyumlu
- **Mobil Kartlar**: Dokunmatik etkileşimli fiyat kartları
- **Organik Göstergeler**: Yeşil yaprak ikonları
- **Trend Analizi**: Fiyat hareketleri görselleştirmesi
- **Otomatik Güncelleme**: Sayfa odaklandığında veri yenileme

## 🎨 Tasarım Özellikleri

- **Gradient Background**: Modern görünüm
- **Card Hover Effects**: Etkileşimli kartlar
- **Color Coding**: Kalite ve trend renk kodlaması
- **Notification System**: Kullanıcı bildirimleri
- **Loading States**: Yükleme durumu göstergeleri

## 📊 Veri Yapısı

Her elma çeşidi için şu bilgiler sunulur:

- **Temel Bilgiler**: İsim, min/max/ortalama fiyat
- **Kalite**: 1. Sınıf / 2. Sınıf
- **Organik Durum**: Organik ürün göstergesi
- **Trend**: Yükseliş/Düşüş/Stabil
- **Volatilite**: Fiyat değişkenliği
- **Detaylar**: Bölge, pazar, sertifikasyon

## 🔄 Otomatik Güncelleme

- **Sayfa Yüklendiğinde**: İlk giriş
- **Sekme Aktif Olduğunda**: Kullanıcı geri döndüğünde
- **Pencere Odaklandığında**: Pencereye tıklandığında
- **5 Dakikada Bir**: Periyodik güncelleme
- **Manuel Yenileme**: "Yenile" butonu

## 🌐 Veri Kaynakları

- **İBB**: https://tarim.ibb.istanbul/avrupa-yakasi-hal-mudurlugu/hal-fiyatlari.html
- **Başak App**: https://basakapp.com/hal-borsa-fiyatlari
- **TOBB**: https://borsa.tobb.org.tr/
- **TMO**: https://www.tmo.gov.tr/

## 📈 İstatistikler

- **8 Elma Çeşidi**: Farklı kalite ve fiyat seviyeleri
- **4 Veri Kaynağı**: Çoklu kaynak entegrasyonu
- **Ultra High Kalite**: %90+ veri kalitesi skoru
- **Gerçek Zamanlı**: Canlı veri güncellemesi

## 🛡️ Güvenlik

- **HTTPS**: Güvenli bağlantı
- **CORS**: Cross-origin resource sharing
- **Input Validation**: Giriş doğrulama
- **Error Handling**: Hata yönetimi

## 📞 Destek

- **Geliştirici**: Tahsin Mert Mutlu
- **WeatherTahsin**: https://weathertahsin.netlify.app
- **Versiyon**: 2.0

## 📄 Lisans

Bu proje açık kaynak kodludur ve eğitim amaçlı kullanılmaktadır.

---

**WeatherTahsin Hal Fiyatları** - Ultra Detaylı Elma Piyasası Takip Sistemi v2.0
