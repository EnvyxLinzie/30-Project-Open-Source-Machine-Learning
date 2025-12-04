"""
Test script to verify Project 10 setup and functionality
Run this to ensure everything is working correctly
"""
import sys
import importlib.util

def check_module(module_name):
    """Check if a module is installed"""
    spec = importlib.util.find_spec(module_name)
    return spec is not None

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("="*60)
    print("Testing Dependencies...")
    print("="*60)
    
    required_modules = [
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'dotenv'
    ]
    
    all_installed = True
    for module in required_modules:
        installed = check_module(module)
        status = "✅" if installed else "❌"
        print(f"{status} {module}")
        if not installed:
            all_installed = False
    
    return all_installed

def test_imports():
    """Test if project modules can be imported"""
    print("\n" + "="*60)
    print("Testing Project Modules...")
    print("="*60)
    
    try:
        from src.data_fetcher import LiquidationDataFetcher
        print("✅ data_fetcher.py")
    except Exception as e:
        print(f"❌ data_fetcher.py: {str(e)}")
        return False
    
    try:
        from src.data_processor import LiquidationDataProcessor
        print("✅ data_processor.py")
    except Exception as e:
        print(f"❌ data_processor.py: {str(e)}")
        return False
    
    try:
        from src.visualizer import LiquidationVisualizer
        print("✅ visualizer.py")
    except Exception as e:
        print(f"❌ visualizer.py: {str(e)}")
        return False
    
    try:
        import config
        print("✅ config.py")
    except Exception as e:
        print(f"❌ config.py: {str(e)}")
        return False
    
    return True

def test_directories():
    """Test if required directories exist"""
    print("\n" + "="*60)
    print("Testing Directory Structure...")
    print("="*60)
    
    import os
    
    required_dirs = [
        'src',
        'data',
        'data/raw',
        'data/processed',
        'results',
        'results/figures',
        'results/reports',
        'notebooks'
    ]
    
    all_exist = True
    for directory in required_dirs:
        exists = os.path.exists(directory)
        status = "✅" if exists else "❌"
        print(f"{status} {directory}/")
        if not exists:
            all_exist = False
    
    return all_exist

def test_config():
    """Test configuration settings"""
    print("\n" + "="*60)
    print("Testing Configuration...")
    print("="*60)
    
    try:
        import config
        
        print(f"✅ API_HOST: {config.API_HOST}")
        print(f"✅ DEFAULT_EXCHANGE: {config.DEFAULT_EXCHANGE}")
        print(f"✅ DEFAULT_PAIR: {config.DEFAULT_PAIR}")
        print(f"✅ LEVERAGE_LEVELS: {config.LEVERAGE_LEVELS}")
        
        if config.API_KEY == "API_KEY":
            print("⚠️  Using default API key - consider setting your own in .env")
        else:
            print("✅ Custom API key configured")
        
        return True
    except Exception as e:
        print(f"❌ Configuration error: {str(e)}")
        return False

def test_sample_data():
    """Test with sample response data"""
    print("\n" + "="*60)
    print("Testing with Sample Data...")
    print("="*60)
    
    try:
        import json
        from src.data_processor import LiquidationDataProcessor
        
        # Load sample response
        with open('response.json', 'r') as f:
            sample_data = json.load(f)
        
        print("✅ Sample data loaded")
        
        # Test processor
        processor = LiquidationDataProcessor(sample_data)
        print(f"✅ Data processor initialized")
        print(f"   Current price: ${processor.current_price:,.2f}")
        print(f"   Leverage levels processed: {len(processor.leverage_data)}")
        
        # Test statistics
        stats = processor.calculate_statistics("100x")
        print(f"✅ Statistics calculated")
        print(f"   Total liquidation: ${stats['total_liquidation_amount']:,.0f}")
        
        return True
    except Exception as e:
        print(f"❌ Sample data test failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("PROJECT 10: LIQUIDATION VISUALIZER - TEST SUITE")
    print("="*60 + "\n")
    
    results = []
    
    # Run tests
    results.append(("Dependencies", test_dependencies()))
    results.append(("Project Modules", test_imports()))
    results.append(("Directory Structure", test_directories()))
    results.append(("Configuration", test_config()))
    results.append(("Sample Data", test_sample_data()))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("="*60)
    print(f"Results: {passed}/{total} tests passed")
    print("="*60)
    
    if passed == total:
        print("\n🎉 All tests passed! Project is ready to run.")
        print("\nNext steps:")
        print("1. Set your API key in .env file")
        print("2. Run: python main.py")
        print("3. Or open: notebooks/liquidation_analysis.ipynb")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nTroubleshooting:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Check file structure matches project layout")
        print("3. Verify all source files are present")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
