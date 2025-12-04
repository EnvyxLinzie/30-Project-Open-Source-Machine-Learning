# Contributing to Project 10: Liquidation Visualizer

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 How to Contribute

### 1. Report Issues
Found a bug or have a feature request?
- Open an issue on GitHub
- Describe the problem clearly
- Include steps to reproduce (for bugs)
- Suggest solutions if possible

### 2. Improve Documentation
- Fix typos or unclear explanations
- Add examples or use cases
- Improve code comments
- Translate documentation

### 3. Add Features
Some ideas for enhancements:
- Support for more exchanges (Bybit, OKX, etc.)
- Historical liquidation analysis
- Real-time WebSocket integration
- ML model to predict liquidation cascades
- Alert system for critical zones
- Multi-pair comparison
- Export to CSV/Excel functionality

### 4. Optimize Code
- Improve performance
- Refactor for better readability
- Add error handling
- Write unit tests

## 🔧 Development Setup

### Fork and Clone
```bash
git fork https://github.com/EnvyxLinzie/30-Project-Open-Source-Machine-Learning.git
git clone https://github.com/YOUR_USERNAME/30-Project-Open-Source-Machine-Learning.git
cd 30-Project-Open-Source-Machine-Learning/Ongoing-Project/Project-10
```

### Create Branch
```bash
git checkout -b feature/your-feature-name
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Example:
```python
def calculate_liquidation_risk(
    price: float,
    leverage: int,
    position_size: float
) -> float:
    """
    Calculate liquidation risk for a position
    
    Args:
        price: Current market price
        leverage: Leverage multiplier
        position_size: Size of position in USD
        
    Returns:
        Risk score between 0 and 1
    """
    # Implementation here
    pass
```

### Documentation
- Update README.md if adding features
- Add docstrings to new functions
- Include usage examples
- Comment complex logic

## 🧪 Testing

Before submitting:
1. Test your code thoroughly
2. Ensure existing functionality still works
3. Add test cases for new features
4. Run the main script: `python main.py`

## 📤 Submitting Changes

### Commit Messages
Use clear, descriptive commit messages:
```bash
git commit -m "Add support for ETH/USDT pair analysis"
git commit -m "Fix: Handle API timeout errors gracefully"
git commit -m "Docs: Update installation instructions"
```

### Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Screenshots (if UI changes)
- Testing performed
- Related issue numbers

## 🎨 Project Structure

When adding new features, maintain the structure:
```
Project-10/
├── src/                    # Source code modules
│   ├── data_fetcher.py    # API interactions
│   ├── data_processor.py  # Data processing
│   └── visualizer.py      # Visualizations
├── notebooks/             # Jupyter notebooks
├── data/                  # Data storage
├── results/               # Output files
├── config.py              # Configuration
└── main.py               # Main script
```

## 🤝 Code Review Process

1. Submit PR with clear description
2. Maintainers review code
3. Address feedback if requested
4. Once approved, PR will be merged
5. Your contribution will be credited!

## 💡 Feature Ideas

### Priority Features:
- [ ] Real-time liquidation tracking
- [ ] Multi-exchange comparison
- [ ] Historical pattern analysis
- [ ] Liquidation cascade prediction model
- [ ] Trading strategy backtesting with liquidation data

### Nice to Have:
- [ ] Dashboard with Streamlit/Dash
- [ ] Email/Telegram alerts
- [ ] Export to various formats
- [ ] API wrapper for easier usage
- [ ] Docker containerization

## 📞 Questions?

- Open a GitHub issue
- Contact via Telegram: [@advancedmicrodevice](https://t.me/advancedmicrodevice)
- Email: ohlc.dev@gmail.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---
Thank you for contributing to the quantitative trading community! 🚀
