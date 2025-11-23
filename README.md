# 30-Project Open-Source Machine Learning 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Data Source](https://img.shields.io/badge/Data-OHLC.dev-green)](https://ohlc.dev)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

![Project Banner](https://via.placeholder.com/1200x300?text=30-Day+Machine+Learning+Challenge+with+OHLC.dev)
*(Banner visual placeholder - Silakan ganti dengan gambar banner project Anda)*

## 🌍 Bahasa / Language
- [Bahasa Indonesia](README.md)
- [English](README_EN.md)

## 📖 Tentang Proyek
Selamat datang di **30-Project Open-Source Machine Learning**! Repositori ini berisi koleksi 30 proyek Machine Learning menggunakan data finansial nyata dari OHLC.dev.

### 🎯 Starter Kit untuk Quantitative Trading
Proyek ini dirancang khusus sebagai **starter kit** untuk siapa saja yang ingin belajar dan mengembangkan sistem **Quantitative Trading**. Di Indonesia, quantitative trading sedang menjadi tren yang sangat populer di kalangan trader dan investor modern. Melalui proyek ini, Anda akan mempelajari cara:
- Menganalisis data pasar secara kuantitatif
- Membangun model prediksi menggunakan Machine Learning
- Mengimplementasikan strategi trading berbasis data
- Melakukan backtesting dan risk management

Tujuan utama proyek ini adalah untuk mengeksplorasi, menganalisis, dan memprediksi pergerakan pasar menggunakan berbagai dataset finansial, mulai dari saham tradisional hingga aset kripto dan sentimen berita. Anda bebas mengerjakan proyek sesuai urutan dan kecepatan Anda sendiri, atau bahkan berkontribusi dengan proyek baru!

### 🔑 API Key Gratis untuk Contributors
**PENTING:** Untuk para contributor yang ingin mengembangkan proyek ini, Anda bisa mendapatkan **API Key GRATIS** dari OHLC.dev! 

📞 **Cara Mendapatkan API Key:**
Hubungi Telegram: [@advancedmicrodevice](https://t.me/advancedmicrodevice)

API key ini khusus untuk keperluan pengembangan proyek open-source ini dan akan memberikan Anda akses penuh ke semua data yang diperlukan.

## 📊 Sumber Data
Seluruh data yang digunakan dalam proyek ini didukung oleh **[OHLC.dev](https://ohlc.dev)**, penyedia API data finansial yang lengkap dan reliabel.

Dataset yang digunakan meliputi:
1.  **OHLC Candle Data**: Data harga (Open, High, Low, Close) untuk berbagai tipe pasar.
2.  **Economic Calendar**: Data kalender ekonomi global untuk analisis fundamental.
3.  **Indonesia Stock Exchange (IDX)**: Data saham khusus pasar Indonesia.
4.  **Crypto Exchange Liquidation**: Data likuidasi dari ±10 exchange kripto besar.
5.  **News Flow API**: Arus berita real-time (judul, isi, deskripsi) untuk analisis sentimen.

## 🗓️ Daftar 30 Proyek Machine Learning

| Proyek | Nama Proyek | Deskripsi | API yang Digunakan | Model Machine Learning |
|:----:|:-----------|:----------|:------------------|:---------------------|
| **Project 1** | Setup Environment | Setup environment Python, Jupyter, dan install library dasar (Pandas, NumPy, Scikit-learn) | - | - |
| **Project 2** | OHLC Data Fetcher | Fetching data OHLC dan visualisasi candlestick sederhana | OHLC Candle Data | - |
| **Project 3** | IDX Sector Analyzer | Analisis performa sektor saham Indonesia (Finance, Mining, Consumer, dll) | IDX Stock Data | K-Means Clustering |
| **Project 4** | Crypto Liquidation Tracker | Eksplorasi data likuidasi dan korelasi dengan volatilitas harga | Crypto Liquidation, OHLC | Statistical Correlation |
| **Project 5** | News Flow Scraper | Fetching berita finansial dan preprocessing teks dasar | News Flow API | Text Preprocessing (NLP) |
| **Project 6** | Data Cleaner | Pembersihan data: handling missing values, outlier detection | All APIs | Data Imputation Techniques |
| **Project 7** | Technical Indicator Builder | Feature engineering indikator teknikal (MA, RSI, MACD, Bollinger) | OHLC Candle Data | - |
| **Project 8** | Crypto-Stock Correlator | Analisis korelasi antara aset kripto dan saham IDX | OHLC, IDX Stock Data | Pearson/Spearman Correlation |
| **Project 9** | Economic Impact Analyzer | Analisis dampak economic calendar terhadap volatilitas pasar | Economic Calendar, OHLC | Event Study Analysis |
| **Project 10** | Liquidation Visualizer | Visualisasi pola likuidasi: kapan trader "rekt"? | Crypto Liquidation | Data Visualization |
| **Project 11** | Basic Sentiment Analyzer | Analisis sentimen berita (Positive/Negative/Neutral) | News Flow API | VADER / TextBlob |
| **Project 12** | Sentiment-Price Merger | Menggabungkan sentimen berita dengan pergerakan harga saham | News Flow API, OHLC | Time-Series Alignment |
| **Project 13** | Anomaly Detector | Deteksi anomali pada transaksi dan pergerakan harga | OHLC, IDX Stock Data | Isolation Forest / Z-Score |
| **Project 14** | EDA Report Generator | Review minggu 2 dan dokumentasi temuan awal | All APIs | - |
| **Project 15** | ARIMA Price Forecaster | Time series forecasting harga menggunakan ARIMA/SARIMA | OHLC Candle Data | ARIMA / SARIMA |
| **Project 16** | Prophet Trend Predictor | Prediksi tren jangka panjang dengan seasonality detection | OHLC Candle Data | Facebook Prophet |
| **Project 17** | LSTM Price Predictor | Deep learning untuk prediksi harga sequential | OHLC Candle Data | LSTM / GRU |
| **Project 18** | Market Trend Classifier | Klasifikasi kondisi pasar (Bullish/Bearish/Sideways) | OHLC, Technical Indicators | Random Forest / XGBoost |
| **Project 19** | Advanced Sentiment Model | Fine-tuning BERT untuk sentimen finansial spesifik | News Flow API | BERT (Fine-tuned) |
| **Project 20** | Hybrid Market Predictor | Prediksi multi-modal: harga + berita + ekonomi | All APIs | Ensemble Learning (Stacking) |
| **Project 21** | Model Evaluator | Evaluasi semua model dengan metrics (RMSE, MAE, F1-Score) | - | Cross-Validation |
| **Project 22** | Backtesting Framework | Membangun framework untuk backtest strategi trading | OHLC Candle Data | Backtesting.py / Custom |
| **Project 23** | Trading Simulator | Simulasi trading berdasarkan prediksi model ML | OHLC Candle Data | Reinforcement Learning (Optional) |
| **Project 24** | Hyperparameter Tuner | Optimasi hyperparameter model terbaik | - | Grid Search / Bayesian Optimization |
| **Project 25** | Interactive Dashboard | Dashboard real-time dengan Streamlit/Dash | All APIs | - |
| **Project 26** | Real-time Data Visualizer | Visualisasi live data dari OHLC.dev API | All APIs | WebSocket / REST API |
| **Project 27** | Portfolio Optimizer | Optimasi portofolio investasi menggunakan ML (Markowitz, Black-Litterman) | IDX Stock Data, OHLC | Mean-Variance Optimization / Genetic Algorithm |
| **Project 28** | Market Regime Detector | Deteksi perubahan regime pasar (Bull/Bear/Sideways Market) | OHLC, Economic Calendar | Hidden Markov Model (HMM) |
| **Project 29** | Risk Management System | Sistem prediksi Value at Risk (VaR) dan Conditional VaR | OHLC, IDX Stock Data | Monte Carlo Simulation / GARCH |
| **Project 30** | Automated Trading Bot | Bot trading otomatis berbasis prediksi ML dengan risk management | All APIs | Reinforcement Learning (DQN/PPO) |

## 🤝 Alur Kontribusi

Kami sangat menyambut kontribusi dari siapa saja! Berikut adalah alur kontribusi yang terstruktur untuk memudahkan kolaborasi:

### 📋 Langkah-langkah Kontribusi:

#### 1️⃣ Clone Repositori
Pertama, clone repositori ini ke local machine Anda:
```bash
git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
cd 30-Project-Open-Source-Machine-Learning
```

#### 2️⃣ Pilih Proyek
Lihat daftar [30 Proyek Machine Learning](#️-daftar-30-proyek-machine-learning) di atas, lalu pilih proyek mana yang ingin Anda kerjakan.

#### 3️⃣ Kerjakan di Folder `Ongoing-Project`
- Buat folder baru dengan nama proyek yang Anda pilih di dalam direktori `Ongoing-Project/`
- Contoh: `Ongoing-Project/Project-03-IDX-Sector-Analyzer/`
- Push pekerjaan Anda ke folder ini agar developer lain bisa berkolaborasi dengan Anda

```bash
# Contoh struktur folder
Ongoing-Project/
  └── Project-03-IDX-Sector-Analyzer/
      ├── data/
      ├── notebooks/
      ├── src/
      └── README.md
```

#### 4️⃣ Kolaborasi dengan Developer Lain
- Developer lain bisa melihat progress Anda dan berkontribusi
- Gunakan Pull Request untuk review kode
- Komunikasikan melalui GitHub Issues

#### 5️⃣ Pindahkan ke `Completed-Project`
Jika proyek sudah **100% selesai** dan telah direview:
- Pindahkan folder proyek dari `Ongoing-Project/` ke `Completed-Project/`
- Pastikan ada dokumentasi lengkap (README, requirements.txt, dll)
- Tambahkan hasil evaluasi model dan kesimpulan

```bash
# Contoh struktur completed project
Completed-Project/
  └── Project-03-IDX-Sector-Analyzer/
      ├── data/
      ├── notebooks/
      ├── src/
      ├── models/
      ├── results/
      ├── README.md
      └── requirements.txt
```

### ✅ Kriteria Proyek "Completed"
Proyek dianggap selesai 100% jika sudah memenuhi:
- ✅ Kode bersih dan terdokumentasi dengan baik
- ✅ Ada README yang menjelaskan cara menjalankan proyek
- ✅ Model ML sudah dilatih dan dievaluasi
- ✅ Ada file requirements.txt atau environment.yml
- ✅ (Opsional) Sudah ada visualisasi hasil atau dashboard

---

## 🚀 Cara Memulai
1.  Clone repositori ini:
    ```bash
    git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Dapatkan API Key gratis di [OHLC.dev](https://ohlc.dev) dan masukkan ke `.env`.
4.  Jalankan notebook hari pertama!

## 🤝 Berkontribusi
Kontribusi sangat diterima! Silakan buka issue atau pull request jika Anda memiliki ide untuk meningkatkan analisis atau model.

## 📄 Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detailnya.

---
*Powered by [OHLC.dev](https://ohlc.dev) - Premium Financial Data API*

## 🌟 Supported by Community

Proyek ini didukung oleh komunitas:
- **[Horizonfx.id](https://horizonfx.id)** - Forex Trading Education & Community
- **[Sixcall.net](https://sixcall.net)** - Trading Technology & Innovation
