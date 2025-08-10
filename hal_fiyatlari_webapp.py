from flask import Flask, render_template, jsonify, request
from hal_fiyatlari_api import TurkiyeHalFiyatlariAPI
import json
from datetime import datetime

app = Flask(__name__)
api = TurkiyeHalFiyatlariAPI()

@app.route('/')
def index():
    """Ana sayfa"""
    return render_template('index.html')

@app.route('/api/fiyatlar')
def get_fiyatlar():
    """Tüm fiyat verilerini döndür"""
    try:
        veriler = api.get_tum_veriler()
        return jsonify(veriler)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/hal-fiyatlari')
def get_hal_fiyatlari():
    """Hal fiyatlarını döndür"""
    try:
        veriler = api.get_manuel_hal_verileri()
        return jsonify(veriler)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/cesit-analizi')
def get_cesit_analizi():
    """Çeşit analizini döndür"""
    try:
        veriler = api.get_elma_cesitleri_fiyatlari()
        return jsonify(veriler)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bolgesel-analiz')
def get_bolgesel_analiz():
    """Bölgesel analizi döndür"""
    try:
        veriler = api.get_bolgesel_fiyat_analizi()
        return jsonify(veriler)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tahmin')
def get_tahmin():
    """Fiyat tahmini döndür"""
    try:
        cesit = request.args.get('cesit', 'Amasya')
        bolge = request.args.get('bolge', 'Marmara')
        tarih_str = request.args.get('tarih')
        
        if tarih_str:
            tarih = datetime.strptime(tarih_str, '%Y-%m-%d')
        else:
            tarih = None
        
        tahmin = api.get_fiyat_tahmini(cesit, bolge, tarih)
        return jsonify(tahmin)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dashboard')
def dashboard():
    """Dashboard sayfası"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
