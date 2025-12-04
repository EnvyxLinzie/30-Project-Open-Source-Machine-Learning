# Installation Guide - Project 10: Liquidation Visualizer

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)

## 🚀 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
cd 30-Project-Open-Source-Machine-Learning/Ongoing-Project/Project-10
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (2.0.0+)
- numpy (1.24.0+)
- matplotlib (3.7.0+)
- seaborn (0.12.0+)
- plotly (5.14.0+)
- requests (2.31.0+)
- python-dotenv (1.0.0+)
- jupyter (1.0.0+)

### 4. Configure API Key

```bash
# Copy example environment file
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Edit .env file and add your API key
# RAPIDAPI_KEY=your_actual_api_key_here
```

**Get Free API Key:**
Contact Telegram: [@advancedmicrodevice](https://t.me/advancedmicrodevice)

### 5. Verify Installation

```bash
python test_project.py
```

You should see:
```
🎉 All tests passed! Project is ready to run.
```

## ✅ Quick Test

Run the main analysis:
```bash
python main.py
```

Expected output:
- Fetches liquidation data from API
- Processes data for all leverage levels
- Generates 4 visualizations
- Saves results to `results/figures/`

## 📊 View Results

After running, check:
- `results/figures/liquidation_heatmap_all.png` - Heatmap for all leverage levels
- `results/figures/leverage_comparison.png` - Comparison charts
- `results/figures/critical_zones_100x.png` - Critical liquidation zones
- `results/figures/interactive_heatmap_100x.html` - Interactive chart (open in browser)

## 🔧 Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Make sure virtual environment is activated and dependencies are installed
```bash
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Issue: API Key Error
**Solution:** Set your API key in `.env` file
```bash
RAPIDAPI_KEY=your_actual_key_here
```

### Issue: Import Error
**Solution:** Run from project root directory
```bash
cd Ongoing-Project/Project-10
python main.py
```

### Issue: Matplotlib Display Error
**Solution:** The script uses non-interactive backend (Agg) by default. Figures are saved to `results/figures/` instead of being displayed.

## 🎓 Next Steps

1. **Explore Jupyter Notebook:**
   ```bash
   jupyter notebook notebooks/liquidation_analysis.ipynb
   ```

2. **Customize Analysis:**
   - Edit `config.py` to change default settings
   - Modify `main.py` to analyze different pairs/exchanges

3. **Read Documentation:**
   - `README.md` - Full project documentation
   - `QUICKSTART.md` - Quick start guide
   - `CONTRIBUTING.md` - Contribution guidelines

## 💡 Tips

- Keep your virtual environment activated when working on the project
- Update dependencies regularly: `pip install --upgrade -r requirements.txt`
- Check `results/` folder for all generated outputs
- Use Jupyter notebook for interactive exploration

## 📞 Support

Need help?
- Open an issue on GitHub
- Contact: [@advancedmicrodevice](https://t.me/advancedmicrodevice)
- Email: ohlc.dev@gmail.com

---
Happy analyzing! 🎉
