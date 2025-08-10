# Türkiye Hal Fiyatları - Elma Piyasası Takip Sistemi

Bu proje, Türkiye'deki hal fiyatları ve elma piyasası verilerini takip etmek için geliştirilmiş kapsamlı bir web uygulamasıdır.

## 🍎 Özellikler

- **Gerçek Zamanlı Fiyat Takibi**: Çeşitli kaynaklardan elma fiyatlarını toplar
- **Bölgesel Analiz**: Türkiye'nin farklı bölgelerindeki fiyat farklılıklarını analiz eder
- **Çeşit Bazlı Analiz**: Farklı elma çeşitlerinin fiyat performansını karşılaştırır
- **Fiyat Tahmini**: Gelecek dönemler için fiyat tahminleri yapar
- **İnteraktif Grafikler**: Chart.js ile görsel veri analizi
- **Responsive Tasarım**: Mobil ve masaüstü uyumlu arayüz

## 📊 Veri Kaynakları

### Resmi Kaynaklar
- **TÜİK (Türkiye İstatistik Kurumu)**: https://data.tuik.gov.tr/
- **Tarım ve Orman Bakanlığı**: https://fiyat.tarimorman.gov.tr/
- **TOBB (Türkiye Odalar ve Borsalar Birliği)**: https://www.tobb.org.tr/

### Özel Veri Sağlayıcıları
- **TARIMBİLGİ**: https://www.tarimbilgi.com/
- **TARIMHABER**: https://www.tarimhaber.com/
- **TARIMDANHABER**: https://www.tarimdanhaber.com/

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- pip (Python paket yöneticisi)

### Adım 1: Projeyi İndirin
```bash
git clone <repository-url>
cd hal-fiyatlari-projesi
```

### Adım 2: Sanal Ortam Oluşturun
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

### Adım 3: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: Uygulamayı Çalıştırın
```bash
python hal_fiyatlari_webapp.py
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

## 📁 Proje Yapısı

```
hal-fiyatlari-projesi/
├── hal_fiyatlari_api.py      # API entegrasyonu ve veri işleme
├── hal_fiyatlari_webapp.py   # Flask web uygulaması
├── requirements.txt          # Python bağımlılıkları
├── README.md                # Bu dosya
├── templates/               # HTML şablonları
│   └── index.html          # Ana sayfa
└── elma_fiyatlari.json     # Örnek veri dosyası (otomatik oluşur)
```

## 🔧 API Kullanımı

### Tüm Verileri Çekme
```python
from hal_fiyatlari_api import TurkiyeHalFiyatlariAPI

api = TurkiyeHalFiyatlariAPI()
tum_veriler = api.get_tum_veriler()
```

### Hal Fiyatları
```python
hal_verileri = api.get_manuel_hal_verileri()
```

### Çeşit Analizi
```python
cesit_analizi = api.get_elma_cesitleri_fiyatlari()
```

### Bölgesel Analiz
```python
bolgesel_analiz = api.get_bolgesel_fiyat_analizi()
```

### Fiyat Tahmini
```python
tahmin = api.get_fiyat_tahmini(
    cesit='Amasya',
    bolge='Marmara',
    tarih=datetime.now()
)
```

## 🌍 Web API Endpoints

### GET /api/fiyatlar
Tüm fiyat verilerini döndürür.

### GET /api/hal-fiyatlari
Hal fiyatlarını döndürür.

### GET /api/cesit-analizi
Çeşit analizini döndürür.

### GET /api/bolgesel-analiz
Bölgesel analizi döndürür.

### GET /api/tahmin?cesit=Amasya&bolge=Marmara&tarih=2024-01-15
Fiyat tahmini döndürür.

## 📈 Elma Çeşitleri

Sistem şu elma çeşitlerini destekler:

- **Amasya**: Geleneksel Türk çeşidi
- **Golden Delicious**: Popüler sarı elma
- **Starking**: Kırmızı elma çeşidi
- **Granny Smith**: Yeşil elma
- **Fuji**: Tatlı elma çeşidi

## 🗺️ Bölgeler

- **Marmara**: İstanbul, Bursa, Tekirdağ
- **İç Anadolu**: Ankara, Konya, Kayseri
- **Ege**: İzmir, Aydın, Manisa
- **Karadeniz**: Trabzon, Samsun, Giresun
- **Akdeniz**: Antalya, Mersin, Adana

## 🔮 Fiyat Tahmin Algoritması

Sistem şu faktörleri dikkate alarak fiyat tahmini yapar:

1. **Çeşit Faktörü**: Her elma çeşidinin piyasa değeri
2. **Bölge Faktörü**: Bölgesel arz-talep dengesi
3. **Mevsim Faktörü**: Yılın hangi döneminde olduğumuz
4. **Tarihsel Veriler**: Geçmiş fiyat trendleri

## 📊 Veri Güncelleme

Veriler şu sıklıklarla güncellenir:
- **Manuel Veriler**: Günlük
- **API Verileri**: Saatlik
- **Tahminler**: Gerçek zamanlı

## 🛠️ Geliştirme

### Yeni Veri Kaynağı Ekleme
1. `hal_fiyatlari_api.py` dosyasına yeni metod ekleyin
2. `get_tum_veriler()` metodunu güncelleyin
3. Web arayüzünü gerekirse güncelleyin

### Yeni Elma Çeşidi Ekleme
1. `get_elma_cesitleri_fiyatlari()` metodunu güncelleyin
2. `get_fiyat_tahmini()` metodundaki faktörleri güncelleyin
3. Web arayüzündeki seçenekleri güncelleyin

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit yapın (`git commit -am 'Yeni özellik eklendi'`)
4. Push yapın (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

- **Geliştirici**: [Adınız]
- **E-posta**: [e-posta@adresiniz.com]
- **GitHub**: [github.com/kullaniciadi]

## 🙏 Teşekkürler

Bu proje şu kaynaklardan veri toplamaktadır:
- TÜİK
- Tarım ve Orman Bakanlığı
- TOBB
- TARIMBİLGİ
- TARIMHABER
- TARIMDANHABER

## 📋 Changelog

### v1.0.0 (2024-01-15)
- İlk sürüm
- Temel API entegrasyonu
- Web arayüzü
- Fiyat tahmin sistemi
- Grafik ve analiz araçları
