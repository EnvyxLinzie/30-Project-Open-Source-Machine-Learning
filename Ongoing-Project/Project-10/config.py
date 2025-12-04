"""
Configuration settings for Liquidation Visualizer
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_API_KEY")
API_HOST = "exchange-liquidation-tracker.p.rapidapi.com"
API_BASE_URL = f"https://{API_HOST}/api"

# Default Parameters
DEFAULT_EXCHANGE = "Bi**ce"
DEFAULT_PAIR = "BTC/USDT"
DEFAULT_TIME_TYPE = "1D"

# Leverage Levels
LEVERAGE_LEVELS = ["10x", "25x", "50x", "100x"]

# Visualization Settings
FIGURE_SIZE = (14, 8)
DPI = 100
COLOR_PALETTE = "viridis"

# File Paths
DATA_DIR = "data"
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
RESULTS_DIR = "results"
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
REPORTS_DIR = os.path.join(RESULTS_DIR, "reports")

# Create directories if they don't exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, FIGURES_DIR, REPORTS_DIR]:
    os.makedirs(directory, exist_ok=True)
