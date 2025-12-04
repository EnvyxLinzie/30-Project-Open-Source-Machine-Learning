"""
Main execution script for Liquidation Visualizer
Project 10: Visualizing liquidation patterns across different leverage levels
"""
import logging
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from src.data_fetcher import LiquidationDataFetcher
from src.data_processor import LiquidationDataProcessor
from src.visualizer import LiquidationVisualizer
import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """
    Main execution function
    """
    try:
        logger.info("="*60)
        logger.info("Project 10: Liquidation Visualizer")
        logger.info("="*60)
        
        # Step 1: Fetch liquidation data
        logger.info("\n[Step 1] Fetching liquidation data...")
        fetcher = LiquidationDataFetcher(api_key=config.API_KEY)
        raw_data = fetcher.fetch_liquidation_map(
            exchange=config.DEFAULT_EXCHANGE,
            pair=config.DEFAULT_PAIR,
            time_type=config.DEFAULT_TIME_TYPE
        )
        
        # Step 2: Process data
        logger.info("\n[Step 2] Processing liquidation data...")
        processor = LiquidationDataProcessor(raw_data)
        
        # Display summary statistics
        logger.info("\n[Step 3] Generating summary statistics...")
        summary = processor.get_liquidation_summary()
        print("\n" + "="*60)
        print("LIQUIDATION SUMMARY - ALL LEVERAGE LEVELS")
        print("="*60)
        print(summary.to_string(index=False))
        print("="*60 + "\n")
        
        # Step 4: Create visualizations
        logger.info("\n[Step 4] Creating visualizations...")
        visualizer = LiquidationVisualizer(processor)
        
        # 4.1: Liquidation heatmap for all leverage levels
        logger.info("Creating liquidation heatmap...")
        visualizer.plot_liquidation_heatmap(
            save_path=f"{config.FIGURES_DIR}/liquidation_heatmap_all.png"
        )
        
        # 4.2: Compare leverage levels
        logger.info("Creating leverage comparison...")
        visualizer.compare_leverage_levels(
            save_path=f"{config.FIGURES_DIR}/leverage_comparison.png"
        )
        
        # 4.3: Identify critical zones for 100x leverage
        logger.info("Identifying critical liquidation zones...")
        visualizer.identify_liquidation_zones(
            leverage="100x",
            top_n=10,
            save_path=f"{config.FIGURES_DIR}/critical_zones_100x.png"
        )
        
        # 4.4: Create interactive heatmap
        logger.info("Creating interactive heatmap...")
        visualizer.create_interactive_heatmap(
            leverage="100x",
            save_path=f"{config.FIGURES_DIR}/interactive_heatmap_100x.html"
        )
        
        logger.info("\n" + "="*60)
        logger.info("Analysis completed successfully!")
        logger.info(f"Results saved to: {config.RESULTS_DIR}/")
        logger.info("="*60)
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise


if __name__ == "__main__":
    main()
