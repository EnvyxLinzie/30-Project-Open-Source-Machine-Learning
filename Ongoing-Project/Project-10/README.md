# Project 10: Liquidation Visualizer 📊

## 🎯 Project Overview
Visualizing liquidation patterns across different leverage levels (10x, 25x, 50x, 100x) to understand when traders get "rekt" in crypto markets. This project analyzes liquidation heatmaps from major crypto exchanges to identify critical price levels where mass liquidations occur.

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Visualizations](#visualizations)
- [Key Insights](#key-insights)
- [Contributing](#contributing)

## ✨ Features
- Fetch real-time liquidation data from crypto exchanges
- Visualize liquidation heatmaps across multiple leverage levels
- Identify critical liquidation zones (support/resistance levels)
- Compare liquidation patterns between different leverage multipliers
- Interactive visualizations with Plotly
- Statistical analysis of liquidation distributions

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
cd 30-Project-Open-Source-Machine-Learning/Ongoing-Project/Project-10

# Install required packages
pip install -r requirements.txt
```

## 📖 Usage

### 1. Fetch Liquidation Data
```python
from src.data_fetcher import LiquidationDataFetcher

# Initialize fetcher
fetcher = LiquidationDataFetcher(api_key="YOUR_API_KEY")

# Fetch data
data = fetcher.fetch_liquidation_map(
    exchange="Bi**ce",
    pair="BTC/USDT",
    time_type="1D"
)
```

### 2. Visualize Liquidation Patterns
```python
from src.visualizer import LiquidationVisualizer

# Initialize visualizer
viz = LiquidationVisualizer(data)

# Create heatmap
viz.plot_liquidation_heatmap()

# Compare leverage levels
viz.compare_leverage_levels()

# Identify critical zones
viz.identify_liquidation_zones()
```

### 3. Run Complete Analysis
```bash
# Run the main analysis script
python main.py
```

## 📁 Project Structure
```
Project-10/
├── data/
│   ├── raw/                    # Raw API responses
│   └── processed/              # Processed liquidation data
├── notebooks/
│   └── liquidation_analysis.ipynb  # Jupyter notebook for exploration
├── src/
│   ├── __init__.py
│   ├── data_fetcher.py        # API data fetching module
│   ├── data_processor.py      # Data processing and cleaning
│   └── visualizer.py          # Visualization functions
├── results/
│   ├── figures/               # Generated plots
│   └── reports/               # Analysis reports
├── main.py                    # Main execution script
├── requirements.txt           # Python dependencies
├── config.py                  # Configuration settings
└── README.md                  # This file
```

## 🔌 Data Source
This project uses the **Exchange Liquidation Tracker API** from RapidAPI:
- **API Endpoint**: `exchange-liquidation-tracker.p.rapidapi.com`
- **Data Type**: Liquidation heatmap data
- **Supported Exchanges**: Binance, Bybit, OKX, and more
- **Leverage Levels**: 10x, 25x, 50x, 100x

### API Response Structure
```json
{
  "liq_10x_map_data": {
    "data": [{
      "liq_price": [...],    // Liquidation price levels
      "liq_level": [...],    // Liquidation amounts (USD)
      "price": [...]         // Current market price
    }]
  },
  "cur_price_data": {
    "data": [{"cur_price": "93201.8"}]
  }
}
```

## 📊 Visualizations

### 1. Liquidation Heatmap
Shows liquidation density across price levels for all leverage multipliers.

### 2. Leverage Comparison
Compares liquidation patterns between 10x, 25x, 50x, and 100x leverage.

### 3. Critical Zone Identification
Highlights price levels with highest liquidation risk.

### 4. Long vs Short Liquidation
Analyzes liquidation distribution for long and short positions.

## 🔍 Key Insights

### What is Liquidation?
Liquidation occurs when a trader's position is forcibly closed because their margin balance falls below the required maintenance margin. Higher leverage = higher liquidation risk.

### When Do Traders Get "Rekt"?
- **High Leverage (100x)**: Liquidations cluster very close to current price
- **Medium Leverage (25x-50x)**: Wider liquidation zones
- **Low Leverage (10x)**: Liquidations spread across broader price range

### Critical Liquidation Zones
Price levels with high liquidation amounts often act as:
- **Support levels** (for long liquidations below current price)
- **Resistance levels** (for short liquidations above current price)

## 🛠️ Technologies Used
- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Static visualizations
- **Plotly**: Interactive visualizations
- **Seaborn**: Statistical data visualization
- **Requests**: HTTP API calls

## 📈 Future Enhancements
- [ ] Real-time liquidation tracking with WebSocket
- [ ] Multi-exchange comparison
- [ ] Historical liquidation pattern analysis
- [ ] Machine learning model to predict liquidation cascades
- [ ] Alert system for critical liquidation zones
- [ ] Integration with trading strategies

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is part of the 30-Project Open-Source Machine Learning initiative and is licensed under the MIT License.

## 📞 Contact
For questions or support:
- **Telegram**: [@advancedmicrodevice](https://t.me/advancedmicrodevice)
- **Email**: ohlc.dev@gmail.com

---
*Part of the [30-Project Open-Source Machine Learning](https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning) initiative*
