# 30-Project Open-Source Machine Learning 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Data Source](https://img.shields.io/badge/Data-OHLC.dev-green)](https://ohlc.dev)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

![Project Banner](https://files.ohlc.dev/hero.png)

## 🌍 Language / Bahasa
- [Bahasa Indonesia](README.md)
- [English](README_EN.md)

## 📖 About the Project
Welcome to **30-Project Open-Source Machine Learning**! This repository contains a collection of 30 Machine Learning projects using real-world financial data from OHLC.dev.

### 🎯 Starter Kit for Quantitative Trading
This project is specifically designed as a **starter kit** for anyone who wants to learn and develop **Quantitative Trading** systems. In Indonesia, quantitative trading is becoming an extremely popular trend among modern traders and investors. Through this project, you will learn how to:
- Analyze market data quantitatively
- Build predictive models using Machine Learning
- Implement data-driven trading strategies
- Perform backtesting and risk management

The main goal of this project is to explore, analyze, and predict market movements using various financial datasets, ranging from traditional stocks to crypto assets and news sentiment. You are free to work on projects in any order and at your own pace, or even contribute new projects!

### 🔑 Free API Keys for Contributors
**IMPORTANT:** For contributors who want to develop this project, you can get a **FREE API Key** from OHLC.dev!

📞 **How to Get an API Key:**
Contact Telegram: [@advancedmicrodevice](https://t.me/advancedmicrodevice)

This API key is specifically for the development of this open-source project and will give you full access to all the data you need.

## 📊 Data Sources
All data used in this project is powered by **[OHLC.dev](https://ohlc.dev)**, a complete and reliable financial data API provider.

Datasets included:
1.  **OHLC Candle Data**: Price data (Open, High, Low, Close) for various market types.
2.  **Economic Calendar**: Global economic calendar data for fundamental analysis.
3.  **Indonesia Stock Exchange (IDX)**: Stock data specifically for the Indonesian market.
4.  **Crypto Exchange Liquidation**: Liquidation data from ~10 major crypto exchanges.
5.  **News Flow API**: Real-time news flow (title, body, description) for sentiment analysis.

## 🗓️ 30 Machine Learning Projects List

| Project | Project Name | Description | API Used | Machine Learning Model |
|:----:|:-----------|:----------|:------------------|:---------------------|
| **Project 1** | Setup Environment | Python environment setup, Jupyter, and install basic libraries (Pandas, NumPy, Scikit-learn) | - | - |
| **Project 2** | OHLC Data Fetcher | Fetching OHLC data and simple candlestick visualization | OHLC Candle Data | - |
| **Project 3** | IDX Sector Analyzer | Performance analysis of Indonesian stock sectors (Finance, Mining, Consumer, etc.) | IDX Stock Data | K-Means Clustering |
| **Project 4** | Crypto Liquidation Tracker | Exploring liquidation data and correlation with price volatility | Crypto Liquidation, OHLC | Statistical Correlation |
| **Project 5** | News Flow Scraper | Fetching financial news and basic text preprocessing | News Flow API | Text Preprocessing (NLP) |
| **Project 6** | Data Cleaner | Data cleaning: handling missing values, outlier detection | All APIs | Data Imputation Techniques |
| **Project 7** | Technical Indicator Builder | Feature engineering of technical indicators (MA, RSI, MACD, Bollinger) | OHLC Candle Data | - |
| **Project 8** | Crypto-Stock Correlator | Correlation analysis between crypto assets and IDX stocks | OHLC, IDX Stock Data | Pearson/Spearman Correlation |
| **Project 9** | Economic Impact Analyzer | Analyzing the impact of economic calendar on market volatility | Economic Calendar, OHLC | Event Study Analysis |
| **Project 10** | Liquidation Visualizer | Visualizing liquidation patterns: when do traders get "rekt"? | Crypto Liquidation | Data Visualization |
| **Project 11** | Basic Sentiment Analyzer | News sentiment analysis (Positive/Negative/Neutral) | News Flow API | VADER / TextBlob |
| **Project 12** | Sentiment-Price Merger | Merging news sentiment with stock price movements | News Flow API, OHLC | Time-Series Alignment |
| **Project 13** | Anomaly Detector | Detecting anomalies in transactions and price movements | OHLC, IDX Stock Data | Isolation Forest / Z-Score |
| **Project 14** | EDA Report Generator | Week 2 review and documentation of initial findings | All APIs | - |
| **Project 15** | ARIMA Price Forecaster | Time series price forecasting using ARIMA/SARIMA | OHLC Candle Data | ARIMA / SARIMA |
| **Project 16** | Prophet Trend Predictor | Long-term trend prediction with seasonality detection | OHLC Candle Data | Facebook Prophet |
| **Project 17** | LSTM Price Predictor | Deep learning for sequential price prediction | OHLC Candle Data | LSTM / GRU |
| **Project 18** | Market Trend Classifier | Market condition classification (Bullish/Bearish/Sideways) | OHLC, Technical Indicators | Random Forest / XGBoost |
| **Project 19** | Advanced Sentiment Model | Fine-tuning BERT for financial-specific sentiment | News Flow API | BERT (Fine-tuned) |
| **Project 20** | Hybrid Market Predictor | Multi-modal prediction: price + news + economy | All APIs | Ensemble Learning (Stacking) |
| **Project 21** | Model Evaluator | Evaluating all models with metrics (RMSE, MAE, F1-Score) | - | Cross-Validation |
| **Project 22** | Backtesting Framework | Building a framework for backtesting trading strategies | OHLC Candle Data | Backtesting.py / Custom |
| **Project 23** | Trading Simulator | Trading simulation based on ML model predictions | OHLC Candle Data | Reinforcement Learning (Optional) |
| **Project 24** | Hyperparameter Tuner | Optimizing hyperparameters of the best models | - | Grid Search / Bayesian Optimization |
| **Project 25** | Interactive Dashboard | Real-time dashboard with Streamlit/Dash | All APIs | - |
| **Project 26** | Real-time Data Visualizer | Live data visualization from OHLC.dev API | All APIs | WebSocket / REST API |
| **Project 27** | Portfolio Optimizer | Investment portfolio optimization using ML (Markowitz, Black-Litterman) | IDX Stock Data, OHLC | Mean-Variance Optimization / Genetic Algorithm |
| **Project 28** | Market Regime Detector | Detecting market regime changes (Bull/Bear/Sideways Market) | OHLC, Economic Calendar | Hidden Markov Model (HMM) |
| **Project 29** | Risk Management System | Value at Risk (VaR) and Conditional VaR prediction system | OHLC, IDX Stock Data | Monte Carlo Simulation / GARCH |
| **Project 30** | Automated Trading Bot | Automated trading bot based on ML predictions with risk management | All APIs | Reinforcement Learning (DQN/PPO) |

## 🤝 Contribution Workflow

We warmly welcome contributions from everyone! Here is a structured contribution workflow to facilitate collaboration:

### 📋 Contribution Steps:

#### 1️⃣ Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
cd 30-Project-Open-Source-Machine-Learning
```

#### 2️⃣ Choose a Project
Check the list of [30 Machine Learning Projects](#️-30-machine-learning-projects-list) above, then choose which project you want to work on.

#### 3️⃣ Work in the `Ongoing-Project` Folder
- Create a new folder with the project name you chose inside the `Ongoing-Project/` directory
- Example: `Ongoing-Project/Project-03-IDX-Sector-Analyzer/`
- Push your work to this folder so other developers can collaborate with you

```bash
# Example folder structure
Ongoing-Project/
  └── Project-03-IDX-Sector-Analyzer/
      ├── data/
      ├── notebooks/
      ├── src/
      └── README.md
```

#### 4️⃣ Collaborate with Other Developers
- Other developers can see your progress and contribute
- Use Pull Requests for code review
- Communicate through GitHub Issues

#### 5️⃣ Move to `Completed-Project`
If the project is **100% complete** and has been reviewed:
- Move the project folder from `Ongoing-Project/` to `Completed-Project/`
- Ensure complete documentation (README, requirements.txt, etc.)
- Add model evaluation results and conclusions

```bash
# Example completed project structure
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

### ✅ "Completed" Project Criteria
A project is considered 100% complete if it meets:
- ✅ Clean and well-documented code
- ✅ README explaining how to run the project
- ✅ ML model trained and evaluated
- ✅ requirements.txt or environment.yml file included
- ✅ (Optional) Results visualization or dashboard

---

## 🚀 Getting Started
1.  Clone this repository:
    ```bash
    git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Get a free API Key at [OHLC.dev](https://ohlc.dev) and add it to your `.env`.
4.  Run the Day 1 notebook!

## 🤝 Contributing
Contributions are welcome! Please open an issue or pull request if you have ideas to improve the analysis or models.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
*Powered by [OHLC.dev](https://ohlc.dev) - Premium Financial Data API*

## 🌟 Supported by Community

This project is supported by the community:
- **[Horizonfx.id](https://horizonfx.id)** - Forex Trading Education & Community
- **[Sixcall.net](https://sixcall.net)** - Cryptocurrency Trading Education & Community

### 💼 Interested in Becoming a Supporter?

We are open to collaboration with companies, communities, or individuals who want to support the development of this open-source project. As a supporter, you will contribute to advancing the quantitative trading and machine learning ecosystem in Indonesia.

**Benefits of Becoming a Supporter:**
- Your company/community logo and profile will be featured in the README
- Exclusive access to the project's development roadmap
- Opportunities to collaborate on custom feature development
- Recognition as a contributor in Indonesia's ML & quant trading community

📬 **Contact Us:**  
If you are interested in becoming a supporter of this project, please contact us via:
- **Telegram:** [@advancedmicrodevice](https://t.me/advancedmicrodevice)
- **Email:** ohlc.dev@gmail.com

Let's build a better quantitative trading ecosystem together!
