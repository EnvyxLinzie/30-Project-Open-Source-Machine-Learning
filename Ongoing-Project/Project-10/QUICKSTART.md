# Quick Start Guide - Liquidation Visualizer

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd Ongoing-Project/Project-10
pip install -r requirements.txt
```

### Step 2: Configure API Key
```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your RapidAPI key
# RAPIDAPI_KEY=your_actual_api_key_here
```

### Step 3: Run the Analysis
```bash
python main.py
```

That's it! The script will:
- ✅ Fetch liquidation data from the API
- ✅ Process data for all leverage levels (10x, 25x, 50x, 100x)
- ✅ Generate visualizations
- ✅ Save results to `results/` folder

## 📊 What You'll Get

### Visualizations Created:
1. **Liquidation Heatmap** - Shows where liquidations cluster
2. **Leverage Comparison** - Compares patterns across leverage levels
3. **Critical Zones** - Identifies top liquidation risk areas
4. **Interactive Chart** - HTML file for interactive exploration

### Output Location:
- Figures: `results/figures/`
- Reports: `results/reports/`
- Raw data: `data/raw/`

## 🔧 Alternative: Use Jupyter Notebook

For interactive exploration:
```bash
jupyter notebook notebooks/liquidation_analysis.ipynb
```

## 💡 Tips

### Analyze Different Trading Pairs:
```python
from src.data_fetcher import LiquidationDataFetcher

fetcher = LiquidationDataFetcher()
data = fetcher.fetch_liquidation_map(
    exchange="Bi**ce",
    pair="ETH/USDT",  # Change pair
    time_type="4H"     # Change timeframe
)
```

### Focus on Specific Leverage:
```python
from src.visualizer import LiquidationVisualizer

visualizer = LiquidationVisualizer(processor)
visualizer.plot_liquidation_heatmap(leverage="100x")
```

### Get Critical Zones:
```python
critical = processor.identify_critical_zones("100x", top_n=5)
print(critical)
```

## 🆘 Troubleshooting

### API Key Error:
- Make sure you've set `RAPIDAPI_KEY` in `.env` file
- Get free API key from: https://rapidapi.com/yasimpratama88/api/exchange-liquidation-tracker

### Import Error:
- Run: `pip install -r requirements.txt`
- Make sure you're in the Project-10 directory

### No Data Returned:
- Check your internet connection
- Verify API key is valid
- Try different exchange or pair

## 📚 Learn More

Read the full [README.md](README.md) for:
- Detailed project documentation
- Data source information
- Advanced usage examples
- Contributing guidelines

---
Happy analyzing! 🎉
