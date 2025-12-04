"""
Data Processor Module for Liquidation Data
Processes and transforms raw liquidation data for analysis
"""
import pandas as pd
import numpy as np
import logging
from typing import Dict, List, Tuple
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LiquidationDataProcessor:
    """
    Processes liquidation data for analysis and visualization
    """
    
    def __init__(self, raw_data: Dict):
        """
        Initialize the data processor
        
        Args:
            raw_data: Raw API response data
        """
        self.raw_data = raw_data
        self.current_price = self._extract_current_price()
        self.leverage_data = {}
        self._process_all_leverage_levels()
    
    def _extract_current_price(self) -> float:
        """
        Extract current market price from raw data
        
        Returns:
            Current price as float
        """
        try:
            cur_price_data = self.raw_data['data']['data']['cur_price_data']
            price = float(cur_price_data['data'][0]['cur_price'])
            logger.info(f"Current price: ${price:,.2f}")
            return price
        except Exception as e:
            logger.error(f"Error extracting current price: {str(e)}")
            return 0.0
    
    def _process_all_leverage_levels(self) -> None:
        """
        Process liquidation data for all leverage levels
        """
        for leverage in config.LEVERAGE_LEVELS:
            try:
                df = self._process_leverage_level(leverage)
                self.leverage_data[leverage] = df
                logger.info(f"Processed {leverage} data: {len(df)} records")
            except Exception as e:
                logger.error(f"Error processing {leverage} data: {str(e)}")
    
    def _process_leverage_level(self, leverage: str) -> pd.DataFrame:
        """
        Process liquidation data for a specific leverage level
        
        Args:
            leverage: Leverage level (e.g., "10x", "25x")
            
        Returns:
            DataFrame with processed liquidation data
        """
        key = f"liq_{leverage}_map_data"
        data = self.raw_data['data']['data'][key]['data'][0]
        
        # Create DataFrame
        df = pd.DataFrame({
            'liq_price': [float(p) for p in data['liq_price']],
            'liq_level': [float(l) for l in data['liq_level']],
            'current_price': [float(p) for p in data['price']]
        })
        
        # Add calculated fields
        df['leverage'] = leverage
        df['distance_from_current'] = df['liq_price'] - self.current_price
        df['distance_pct'] = (df['distance_from_current'] / self.current_price) * 100
        df['position_type'] = df['liq_price'].apply(
            lambda x: 'Long' if x < self.current_price else 'Short'
        )
        
        # Sort by liquidation price
        df = df.sort_values('liq_price').reset_index(drop=True)
        
        return df
    
    def get_leverage_data(self, leverage: str) -> pd.DataFrame:
        """
        Get processed data for specific leverage level
        
        Args:
            leverage: Leverage level (e.g., "10x")
            
        Returns:
            DataFrame with liquidation data
        """
        return self.leverage_data.get(leverage, pd.DataFrame())
    
    def get_all_leverage_data(self) -> pd.DataFrame:
        """
        Combine all leverage levels into single DataFrame
        
        Returns:
            Combined DataFrame with all leverage data
        """
        all_data = []
        for leverage, df in self.leverage_data.items():
            all_data.append(df)
        
        return pd.concat(all_data, ignore_index=True)
    
    def identify_critical_zones(
        self,
        leverage: str,
        top_n: int = 10
    ) -> pd.DataFrame:
        """
        Identify critical liquidation zones with highest amounts
        
        Args:
            leverage: Leverage level to analyze
            top_n: Number of top zones to return
            
        Returns:
            DataFrame with top liquidation zones
        """
        df = self.get_leverage_data(leverage)
        
        # Get top liquidation zones
        critical_zones = df.nlargest(top_n, 'liq_level')
        
        return critical_zones[['liq_price', 'liq_level', 'position_type', 'distance_pct']]
    
    def calculate_statistics(self, leverage: str) -> Dict:
        """
        Calculate statistical metrics for liquidation data
        
        Args:
            leverage: Leverage level to analyze
            
        Returns:
            Dictionary with statistical metrics
        """
        df = self.get_leverage_data(leverage)
        
        long_liq = df[df['position_type'] == 'Long']
        short_liq = df[df['position_type'] == 'Short']
        
        stats = {
            'total_liquidation_amount': df['liq_level'].sum(),
            'long_liquidation_amount': long_liq['liq_level'].sum(),
            'short_liquidation_amount': short_liq['liq_level'].sum(),
            'avg_liquidation_amount': df['liq_level'].mean(),
            'max_liquidation_amount': df['liq_level'].max(),
            'num_liquidation_levels': len(df),
            'price_range': (df['liq_price'].min(), df['liq_price'].max()),
            'long_short_ratio': long_liq['liq_level'].sum() / short_liq['liq_level'].sum()
            if short_liq['liq_level'].sum() > 0 else 0
        }
        
        return stats
    
    def get_liquidation_summary(self) -> pd.DataFrame:
        """
        Get summary statistics for all leverage levels
        
        Returns:
            DataFrame with summary statistics
        """
        summary_data = []
        
        for leverage in config.LEVERAGE_LEVELS:
            stats = self.calculate_statistics(leverage)
            stats['leverage'] = leverage
            summary_data.append(stats)
        
        return pd.DataFrame(summary_data)
