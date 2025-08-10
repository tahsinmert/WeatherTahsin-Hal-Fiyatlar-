import requests
import json
from datetime import datetime, timedelta
import time

class TurkiyeHalFiyatlariAPI:
    """
    Türkiye Hal Fiyatları API Entegrasyonu
    Çeşitli kaynaklardan elma fiyatlarını çeker
    """
    
    def __init__(self):
        self.tuik_api_url = "https://api.tuik.gov.tr/api"
        self.tarim_bilgi_url = "https://www.tarimbilgi.com/api"
        self.fiyat_tarim_url = "https://fiyat.tarimorman.gov.tr/api"
        
        # API anahtarları (gerekirse)
        self.api_keys = {
            'tuik': None,  # TÜİK API anahtarı
            'tarim_bilgi': None,  # TarımBilgi API anahtarı
        }
        
        # Cache için
        self.cache = {}
        self.cache_duration = 3600  # 1 saat
    
    def get_tuik_elma_fiyatlari(self, il_adi=None, tarih_baslangic=None, tarih_bitis=None):
        """
        TÜİK'ten elma fiyatlarını çeker
        """
        try:
            # TÜİK API endpoint'i (örnek)
            endpoint = f"{self.tuik_api_url}/tarim/urun-fiyatlari"
            
            params = {
                'urun': 'elma',
                'format': 'json'
            }
            
            if il_adi:
                params['il'] = il_adi
            if tarih_baslangic:
                params['baslangic_tarih'] = tarih_baslangic
            if tarih_bitis:
                params['bitis_tarih'] = tarih_bitis
            
            response = requests.get(endpoint, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_tuik_data(data)
            else:
                print(f"TÜİK API Hatası: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"TÜİK veri çekme hatası: {e}")
            return None
    
    def get_tarim_bilgi_elma_fiyatlari(self, bolge=None):
        """
        TarımBilgi'den elma fiyatlarını çeker
        """
        try:
            # TarımBilgi API endpoint'i (örnek)
            endpoint = f"{self.tarim_bilgi_url}/fiyatlar/elma"
            
            params = {}
            if bolge:
                params['bolge'] = bolge
            
            headers = {}
            if self.api_keys['tarim_bilgi']:
                headers['Authorization'] = f"Bearer {self.api_keys['tarim_bilgi']}"
            
            response = requests.get(endpoint, params=params, headers=headers, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_tarim_bilgi_data(data)
            else:
                print(f"TarımBilgi API Hatası: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"TarımBilgi veri çekme hatası: {e}")
            return None
    
    def get_manuel_hal_verileri(self):
        """
        Manuel olarak toplanan hal verileri (örnek veriler)
        """
        return {
            'kaynak': 'Manuel Veri Toplama',
            'tarih': datetime.now().strftime('%Y-%m-%d'),
            'veriler': [
                {
                    'il': 'İstanbul',
                    'hal': 'Marmara Hal',
                    'urun': 'Amasya Elması',
                    'min_fiyat': 8.50,
                    'max_fiyat': 12.00,
                    'ortalama_fiyat': 10.25,
                    'birim': 'TL/kg',
                    'kalite': '1. Sınıf'
                },
                {
                    'il': 'İstanbul',
                    'hal': 'Marmara Hal',
                    'urun': 'Golden Delicious',
                    'min_fiyat': 9.00,
                    'max_fiyat': 13.50,
                    'ortalama_fiyat': 11.25,
                    'birim': 'TL/kg',
                    'kalite': '1. Sınıf'
                },
                {
                    'il': 'Ankara',
                    'hal': 'Ankara Hal',
                    'urun': 'Amasya Elması',
                    'min_fiyat': 7.50,
                    'max_fiyat': 11.00,
                    'ortalama_fiyat': 9.25,
                    'birim': 'TL/kg',
                    'kalite': '1. Sınıf'
                },
                {
                    'il': 'İzmir',
                    'hal': 'İzmir Hal',
                    'urun': 'Golden Delicious',
                    'min_fiyat': 8.00,
                    'max_fiyat': 12.50,
                    'ortalama_fiyat': 10.25,
                    'birim': 'TL/kg',
                    'kalite': '1. Sınıf'
                }
            ]
        }
    
    def get_elma_cesitleri_fiyatlari(self):
        """
        Elma çeşitlerine göre fiyat analizi
        """
        cesitler = {
            'Amasya': {
                'min_fiyat': 7.50,
                'max_fiyat': 12.00,
                'ortalama': 9.75,
                'populerlik': 'Yüksek',
                'kalite': 'Premium'
            },
            'Golden Delicious': {
                'min_fiyat': 8.00,
                'max_fiyat': 13.50,
                'ortalama': 10.75,
                'populerlik': 'Çok Yüksek',
                'kalite': 'Premium'
            },
            'Starking': {
                'min_fiyat': 7.00,
                'max_fiyat': 11.50,
                'ortalama': 9.25,
                'populerlik': 'Orta',
                'kalite': 'Standart'
            },
            'Granny Smith': {
                'min_fiyat': 8.50,
                'max_fiyat': 14.00,
                'ortalama': 11.25,
                'populerlik': 'Yüksek',
                'kalite': 'Premium'
            },
            'Fuji': {
                'min_fiyat': 9.00,
                'max_fiyat': 15.00,
                'ortalama': 12.00,
                'populerlik': 'Orta',
                'kalite': 'Premium'
            }
        }
        
        return cesitler
    
    def get_bolgesel_fiyat_analizi(self):
        """
        Bölgesel fiyat analizi
        """
        bolgeler = {
            'Marmara': {
                'ortalama_fiyat': 10.50,
                'trend': 'Yükseliş',
                'arz_durumu': 'Yeterli',
                'talep_durumu': 'Yüksek'
            },
            'İç Anadolu': {
                'ortalama_fiyat': 9.25,
                'trend': 'Stabil',
                'arz_durumu': 'Bol',
                'talep_durumu': 'Orta'
            },
            'Ege': {
                'ortalama_fiyat': 10.00,
                'trend': 'Hafif Yükseliş',
                'arz_durumu': 'Yeterli',
                'talep_durumu': 'Yüksek'
            },
            'Karadeniz': {
                'ortalama_fiyat': 8.75,
                'trend': 'Stabil',
                'arz_durumu': 'Bol',
                'talep_durumu': 'Orta'
            },
            'Akdeniz': {
                'ortalama_fiyat': 11.25,
                'trend': 'Yükseliş',
                'arz_durumu': 'Sınırlı',
                'talep_durumu': 'Çok Yüksek'
            }
        }
        
        return bolgeler
    
    def get_fiyat_tahmini(self, cesit='Amasya', bolge='Marmara', tarih=None):
        """
        Gelecek fiyat tahmini
        """
        if tarih is None:
            tarih = datetime.now() + timedelta(days=30)
        
        # Basit tahmin algoritması
        base_price = 10.00
        
        # Çeşit faktörü
        cesit_faktorleri = {
            'Amasya': 1.0,
            'Golden Delicious': 1.1,
            'Starking': 0.95,
            'Granny Smith': 1.15,
            'Fuji': 1.25
        }
        
        # Bölge faktörü
        bolge_faktorleri = {
            'Marmara': 1.05,
            'İç Anadolu': 0.95,
            'Ege': 1.0,
            'Karadeniz': 0.9,
            'Akdeniz': 1.1
        }
        
        # Mevsim faktörü
        ay = tarih.month
        if ay in [9, 10, 11]:  # Sonbahar - hasat sezonu
            mevsim_faktoru = 0.9
        elif ay in [12, 1, 2]:  # Kış - depolama
            mevsim_faktoru = 1.1
        elif ay in [3, 4, 5]:  # İlkbahar - az arz
            mevsim_faktoru = 1.2
        else:  # Yaz
            mevsim_faktoru = 1.0
        
        tahmin_fiyat = base_price * cesit_faktorleri.get(cesit, 1.0) * \
                      bolge_faktorleri.get(bolge, 1.0) * mevsim_faktoru
        
        return {
            'cesit': cesit,
            'bolge': bolge,
            'tahmin_tarih': tarih.strftime('%Y-%m-%d'),
            'tahmin_fiyat': round(tahmin_fiyat, 2),
            'birim': 'TL/kg',
            'guvenilirlik': 'Orta'
        }
    
    def _parse_tuik_data(self, data):
        """
        TÜİK verilerini parse eder
        """
        # TÜİK veri formatına göre parse işlemi
        return data
    
    def _parse_tarim_bilgi_data(self, data):
        """
        TarımBilgi verilerini parse eder
        """
        # TarımBilgi veri formatına göre parse işlemi
        return data
    
    def get_tum_veriler(self):
        """
        Tüm kaynaklardan veri çeker
        """
        veriler = {
            'tarih': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'manuel_veriler': self.get_manuel_hal_verileri(),
            'cesit_analizi': self.get_elma_cesitleri_fiyatlari(),
            'bolgesel_analiz': self.get_bolgesel_fiyat_analizi(),
            'tahminler': {}
        }
        
        # Çeşit ve bölge kombinasyonları için tahminler
        cesitler = ['Amasya', 'Golden Delicious', 'Starking', 'Granny Smith', 'Fuji']
        bolgeler = ['Marmara', 'İç Anadolu', 'Ege', 'Karadeniz', 'Akdeniz']
        
        for cesit in cesitler:
            veriler['tahminler'][cesit] = {}
            for bolge in bolgeler:
                veriler['tahminler'][cesit][bolge] = self.get_fiyat_tahmini(cesit, bolge)
        
        return veriler

# Kullanım örneği
if __name__ == "__main__":
    api = TurkiyeHalFiyatlariAPI()
    
    # Tüm verileri çek
    tum_veriler = api.get_tum_veriler()
    
    # JSON olarak kaydet
    with open('elma_fiyatlari.json', 'w', encoding='utf-8') as f:
        json.dump(tum_veriler, f, ensure_ascii=False, indent=2)
    
    print("Elma fiyatları verileri 'elma_fiyatlari.json' dosyasına kaydedildi.")
    
    # Örnek kullanım
    print("\n=== ELMA FİYATLARI RAPORU ===")
    print(f"Rapor Tarihi: {tum_veriler['tarih']}")
    
    print("\n--- Hal Fiyatları ---")
    for veri in tum_veriler['manuel_veriler']['veriler']:
        print(f"{veri['il']} - {veri['hal']}: {veri['urun']} - {veri['ortalama_fiyat']} {veri['birim']}")
    
    print("\n--- Çeşit Analizi ---")
    for cesit, bilgi in tum_veriler['cesit_analizi'].items():
        print(f"{cesit}: {bilgi['ortalama']} TL/kg ({bilgi['populerlik']} popülerlik)")
    
    print("\n--- Bölgesel Analiz ---")
    for bolge, bilgi in tum_veriler['bolgesel_analiz'].items():
        print(f"{bolge}: {bilgi['ortalama_fiyat']} TL/kg - Trend: {bilgi['trend']}")
