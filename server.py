from flask import Flask, send_from_directory, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    """Ana sayfa - index.html dosyasını serve et"""
    return send_from_directory('.', 'index.html')

@app.route('/ibb_elma_fiyatlari.json')
def get_elma_fiyatlari():
    """Elma fiyatları JSON verisini döndür (eski format uyumluluğu için)"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Eski format uyumluluğu için dönüştür
        legacy_data = {
            'kaynaklar': [data['metadata']['data_quality_level']],
            'urls': ['Ultra Detaylı Veri'],
            'tarih': data['metadata']['data_collection_time'],
            'guncel_fiyatlar': []
        }
        
        for item in data['aggregated_data']:
            legacy_item = {
                'urun_adi': item['name'],
                'min_fiyat': item['min_price'],
                'max_fiyat': item['max_price'],
                'ortalama_fiyat': item['avg_price'],
                'birim': item['unit'],
                'kalite': item['quality'],
                'hal': item['market'],
                'kaynak': 'Ultra Detaylı Sistem',
                'son_guncelleme': data['metadata']['data_collection_time'].split(' ')[0]
            }
            legacy_data['guncel_fiyatlar'].append(legacy_item)
        
        return jsonify(legacy_data)
    except FileNotFoundError:
        return jsonify({'error': 'Veri dosyası bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ultra_detayli_elma_fiyatlari.json')
def get_ultra_detayli_elma_fiyatlari():
    """Ultra detaylı elma fiyatları JSON verisini döndür"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'Ultra detaylı veri dosyası bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/refresh')
def refresh_data():
    """Verileri manuel olarak yenile"""
    try:
        # Scraper'ı çalıştır
        import subprocess
        result = subprocess.run(['python3', 'hal_fiyatlari_scraper.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Ultra detaylı veriler başarıyla güncellendi',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'data_file': 'ultra_detayli_elma_fiyatlari.json'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.stderr
            }), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/statistics')
def get_statistics():
    """Detaylı istatistikleri döndür"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'statistics': data.get('statistics', {}),
            'quality_metrics': data.get('quality_metrics', {}),
            'metadata': data.get('metadata', {})
        })
    except FileNotFoundError:
        return jsonify({'error': 'Veri dosyası bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sources')
def get_sources():
    """Veri kaynakları bilgilerini döndür"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'sources': data.get('sources', {}),
            'source_count': len(data.get('sources', {})),
            'successful_sources': len([s for s in data.get('sources', {}).values() if 'error' not in s])
        })
    except FileNotFoundError:
        return jsonify({'error': 'Veri dosyası bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products')
def get_products():
    """Ürün listesini döndür"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'products': data.get('aggregated_data', []),
            'total_count': len(data.get('aggregated_data', [])),
            'quality_distribution': data.get('statistics', {}).get('quality_distribution', {}),
            'regional_distribution': data.get('statistics', {}).get('regional_distribution', {})
        })
    except FileNotFoundError:
        return jsonify({'error': 'Veri dosyası bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Sağlık kontrolü"""
    try:
        with open('ultra_detayli_elma_fiyatlari.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'service': 'Ultra Detaylı Hal Fiyatları API',
            'data_quality': data.get('metadata', {}).get('data_quality_level', 'Unknown'),
            'product_count': len(data.get('aggregated_data', [])),
            'source_count': data.get('metadata', {}).get('data_sources_count', 0)
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'service': 'Ultra Detaylı Hal Fiyatları API'
        }), 500

if __name__ == '__main__':
    print("🚀 Ultra Detaylı Hal Fiyatları Web Sunucusu başlatılıyor...")
    print("Web sayfası: http://localhost:5000")
    print("Eski format API: http://localhost:5000/ibb_elma_fiyatlari.json")
    print("Yeni format API: http://localhost:5000/ultra_detayli_elma_fiyatlari.json")
    print("İstatistikler: http://localhost:5000/api/statistics")
    print("Veri kaynakları: http://localhost:5000/api/sources")
    print("Ürün listesi: http://localhost:5000/api/products")
    print("Veri yenileme: http://localhost:5000/api/refresh")
    print("Sağlık kontrolü: http://localhost:5000/health")
    print("\nSunucuyu durdurmak için Ctrl+C tuşlayın.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
