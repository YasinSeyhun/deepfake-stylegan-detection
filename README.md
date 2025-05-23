# Deepfake Detection with StyleGAN-generated Faces

Bu proje, gerçek ve sahte (deepfake) yüz görsellerini ayırt edebilen bir makine öğrenimi modeli geliştirmeyi amaçlar. Sahte yüzler StyleGAN ile üretilmiş, gerçek yüzler ise FFHQ veri setinden alınmıştır. Proje, eğitimden web arayüzüne kadar uçtan uca bir pipeline sunar.

## Klasör Yapısı

```
deeepfake-stylegan-detection/
│
├── data/                  # Ham ve işlenmiş veri setleri
│   ├── raw/               # Orijinal, işlenmemiş veri (FFHQ, deepfake)
│   ├── processed/         # Eğitim/validasyon/test için işlenmiş veri
│   └── samples/           # Örnek görseller (sunum için)
│
├── notebooks/             # Veri analizi ve deneme Jupyter notebookları
│
├── src/                   # Tüm ana kodlar
│   ├── data/              # Veri hazırlama, augmentasyon scriptleri
│   │   ├── prepare_data.py
│   │   └── augment.py
│   ├── models/            # Model mimarileri ve eğitim scriptleri
│   │   ├── detector.py
│   │   └── train.py
│   ├── inference/         # Tahmin ve değerlendirme scriptleri
│   │   ├── predict.py
│   │   └── evaluate.py
│   └── utils/             # Yardımcı fonksiyonlar (görselleştirme, config vs.)
│       └── helpers.py
│
├── webapp/                # Web arayüzü (Flask veya Streamlit)
│   ├── static/            # CSS, JS, görseller
│   ├── templates/         # HTML şablonları
│   └── app.py             # Ana web uygulaması
│
├── models/                # Eğitilmiş model ağırlıkları
│
├── tests/                 # Otomatik testler (unit, integration)
│
├── requirements.txt       # Gerekli Python paketleri
├── .gitignore             # Gereksiz dosyaları dışarıda tutmak için
└── README.md              # Proje açıklaması ve kullanım talimatları
```

## Kısa Kurulum

1. Python 3.9 kurulu olmalı.
2. `pip install -r requirements.txt` ile bağımlılıkları yükleyin.
3. `data/raw` klasörüne FFHQ ve deepfake görsellerinizi yerleştirin.
4. Eğitim ve test için `src/data/prepare_data.py` scriptini çalıştırın.
5. Modeli eğitmek için `src/models/train.py` scriptini kullanın.
6. Web arayüzünü başlatmak için `webapp/app.py` dosyasını çalıştırın.

Detaylar için kod ve dökümantasyonlara bakınız. #   d e e p f a k e - s t y l e g a n - d e t e c t i o n  
 