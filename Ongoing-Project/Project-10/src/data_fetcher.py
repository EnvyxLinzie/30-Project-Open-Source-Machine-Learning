"""
Data Fetcher Module for Liquidation Data
Handles API requests to fetch liquidation heatmap data from crypto exchanges
"""
import http.client
import json
import logging
from typing import Dict, Optional
from datetime import datetime
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LiquidationDataFetcher:
    """
    Fetches liquidation data from Exchange Liquidation Tracker API
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the data fetcher
        
        Args:
            api_key: RapidAPI key for authentication
        """
        self.api_key = api_key or config.API_KEY
        self.api_host = config.API_HOST
        
    def fetch_liquidation_map(
        self,
        exchange: str = config.DEFAULT_EXCHANGE,
        pair: str = config.DEFAULT_PAIR,
        time_type: str = config.DEFAULT_TIME_TYPE
    ) -> Dict:
        """
        Fetch liquidation heatmap data from the API
        
        Args:
            exchange: Exchange name (e.g., "Bi**ce")
            pair: Trading pair (e.g., "BTC/USDT")
            time_type: Time period (e.g., "1D", "4H")
            
        Returns:
            Dictionary containing liquidation data
        """
        try:
            logger.info(f"Fetching liquidation data for {pair} on {exchange}")
            
            # Establish connection
            conn = http.client.HTTPSConnection(self.api_host)
            
            # Set headers
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            # Build endpoint URL
            endpoint = f"/api/liquidity-map?exchange={exchange}&pair={pair}&timeType={time_type}"
            
            # Make request
            conn.request("GET", endpoint, headers=headers)
            res = conn.getresponse()
            data = res.read()
            
            # Parse response
            response_data = json.loads(data.decode("utf-8"))
            
            # Validate response
            if not response_data.get("success"):
                raise ValueError("API request failed")
            
            logger.info("Successfully fetched liquidation data")
            
            # Save raw data
            self._save_raw_data(response_data, exchange, pair, time_type)
            
            return response_data
            
        except Exception as e:
            logger.error(f"Error fetching liquidation data: {str(e)}")
            raise
        finally:
            conn.close()
    
    def _save_raw_data(
        self,
        data: Dict,
        exchange: str,
        pair: str,
        time_type: str
    ) -> None:
        """
        Save raw API response to file
        
        Args:
            data: API response data
            exchange: Exchange name
            pair: Trading pair
            time_type: Time period
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pair_clean = pair.replace("/", "_")
            filename = f"{exchange}_{pair_clean}_{time_type}_{timestamp}.json"
            filepath = f"{config.RAW_DATA_DIR}/{filename}"
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Raw data saved to {filepath}")
            
        except Exception as e:
            logger.warning(f"Failed to save raw data: {str(e)}")
    
    def fetch_multiple_timeframes(
        self,
        exchange: str = config.DEFAULT_EXCHANGE,
        pair: str = config.DEFAULT_PAIR,
        timeframes: list = ["1d", "7d", "30D"]
    ) -> Dict[str, Dict]:
        """
        Fetch liquidation data for multiple timeframes
        
        Args:
            exchange: Exchange name
            pair: Trading pair
            timeframes: List of timeframes to fetch
            
        Returns:
            Dictionary with timeframe as key and data as value
        """
        results = {}
        
        for timeframe in timeframes:
            try:
                data = self.fetch_liquidation_map(exchange, pair, timeframe)
                results[timeframe] = data
            except Exception as e:
                logger.error(f"Failed to fetch data for {timeframe}: {str(e)}")
                
        return results
