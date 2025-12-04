"""
Visualization Module for Liquidation Data
Creates various visualizations to analyze liquidation patterns
"""
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import logging
from typing import Optional, List
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = config.FIGURE_SIZE
plt.rcParams['figure.dpi'] = config.DPI


class LiquidationVisualizer:
    """
    Creates visualizations for liquidation data analysis
    """
    
    def __init__(self, processor):
        """
        Initialize the visualizer
        
        Args:
            processor: LiquidationDataProcessor instance
        """
        self.processor = processor
        self.current_price = processor.current_price
    
    def plot_liquidation_heatmap(
        self,
        leverage: Optional[str] = None,
        save_path: Optional[str] = None
    ) -> None:
        """
        Create liquidation heatmap visualization
        
        Args:
            leverage: Specific leverage level or None for all
            save_path: Path to save the figure
        """
        try:
            if leverage:
                df = self.processor.get_leverage_data(leverage)
                self._plot_single_heatmap(df, leverage, save_path)
            else:
                self._plot_all_leverage_heatmap(save_path)
                
            logger.info("Liquidation heatmap created successfully")
            
        except Exception as e:
            logger.error(f"Error creating heatmap: {str(e)}")
    
    def _plot_single_heatmap(
        self,
        df: pd.DataFrame,
        leverage: str,
        save_path: Optional[str]
    ) -> None:
        """Plot heatmap for single leverage level"""
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Separate long and short positions
        long_df = df[df['position_type'] == 'Long']
        short_df = df[df['position_type'] == 'Short']
        
        # Plot liquidation levels
        ax.bar(long_df['liq_price'], long_df['liq_level'], 
               width=50, color='red', alpha=0.6, label='Long Liquidations')
        ax.bar(short_df['liq_price'], short_df['liq_level'],
               width=50, color='green', alpha=0.6, label='Short Liquidations')
        
        # Add current price line
        ax.axvline(self.current_price, color='blue', linestyle='--',
                   linewidth=2, label=f'Current Price: ${self.current_price:,.0f}')
        
        ax.set_xlabel('Price (USD)', fontsize=12)
        ax.set_ylabel('Liquidation Amount (USD)', fontsize=12)
        ax.set_title(f'Liquidation Heatmap - {leverage} Leverage', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

    def _plot_all_leverage_heatmap(self, save_path: Optional[str]) -> None:
        """Plot heatmap for all leverage levels"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        for idx, leverage in enumerate(config.LEVERAGE_LEVELS):
            df = self.processor.get_leverage_data(leverage)
            ax = axes[idx]
            
            long_df = df[df['position_type'] == 'Long']
            short_df = df[df['position_type'] == 'Short']
            
            ax.bar(long_df['liq_price'], long_df['liq_level'],
                   width=50, color='red', alpha=0.6, label='Long')
            ax.bar(short_df['liq_price'], short_df['liq_level'],
                   width=50, color='green', alpha=0.6, label='Short')
            ax.axvline(self.current_price, color='blue', linestyle='--',
                       linewidth=2, label='Current Price')
            
            ax.set_xlabel('Price (USD)')
            ax.set_ylabel('Liquidation Amount (USD)')
            ax.set_title(f'{leverage} Leverage', fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        plt.suptitle('Liquidation Heatmap - All Leverage Levels',
                     fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def compare_leverage_levels(self, save_path: Optional[str] = None) -> None:
        """Compare liquidation patterns across leverage levels"""
        try:
            summary = self.processor.get_liquidation_summary()
            
            fig, axes = plt.subplots(2, 2, figsize=(14, 10))
            
            # Total liquidation amount
            axes[0, 0].bar(summary['leverage'], summary['total_liquidation_amount'],
                           color='steelblue')
            axes[0, 0].set_title('Total Liquidation Amount by Leverage')
            axes[0, 0].set_ylabel('Amount (USD)')
            axes[0, 0].tick_params(axis='x', rotation=0)
            
            # Long vs Short
            x = np.arange(len(summary))
            width = 0.35
            axes[0, 1].bar(x - width/2, summary['long_liquidation_amount'],
                           width, label='Long', color='red', alpha=0.7)
            axes[0, 1].bar(x + width/2, summary['short_liquidation_amount'],
                           width, label='Short', color='green', alpha=0.7)
            axes[0, 1].set_title('Long vs Short Liquidations')
            axes[0, 1].set_xticks(x)
            axes[0, 1].set_xticklabels(summary['leverage'])
            axes[0, 1].legend()
            
            # Number of liquidation levels
            axes[1, 0].bar(summary['leverage'], summary['num_liquidation_levels'],
                           color='coral')
            axes[1, 0].set_title('Number of Liquidation Levels')
            axes[1, 0].set_ylabel('Count')
            
            # Long/Short Ratio
            axes[1, 1].bar(summary['leverage'], summary['long_short_ratio'],
                           color='purple', alpha=0.7)
            axes[1, 1].set_title('Long/Short Liquidation Ratio')
            axes[1, 1].axhline(y=1, color='black', linestyle='--', alpha=0.5)
            axes[1, 1].set_ylabel('Ratio')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()
            
            logger.info("Leverage comparison created successfully")
            
        except Exception as e:
            logger.error(f"Error creating leverage comparison: {str(e)}")

    def identify_liquidation_zones(
        self,
        leverage: str = "100x",
        top_n: int = 10,
        save_path: Optional[str] = None
    ) -> None:
        """Identify and visualize critical liquidation zones"""
        try:
            critical_zones = self.processor.identify_critical_zones(leverage, top_n)
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
            
            # Bar chart of top liquidation zones
            colors = ['red' if pt == 'Long' else 'green' 
                     for pt in critical_zones['position_type']]
            ax1.barh(range(len(critical_zones)), critical_zones['liq_level'],
                     color=colors, alpha=0.7)
            ax1.set_yticks(range(len(critical_zones)))
            ax1.set_yticklabels([f"${p:,.0f}" for p in critical_zones['liq_price']])
            ax1.set_xlabel('Liquidation Amount (USD)')
            ax1.set_title(f'Top {top_n} Critical Liquidation Zones - {leverage}')
            ax1.invert_yaxis()
            
            # Distance from current price
            ax2.barh(range(len(critical_zones)), critical_zones['distance_pct'],
                     color=colors, alpha=0.7)
            ax2.set_yticks(range(len(critical_zones)))
            ax2.set_yticklabels([f"${p:,.0f}" for p in critical_zones['liq_price']])
            ax2.set_xlabel('Distance from Current Price (%)')
            ax2.set_title('Distance from Current Price')
            ax2.axvline(x=0, color='blue', linestyle='--', linewidth=2)
            ax2.invert_yaxis()
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()
            
            # Print summary
            print(f"\n{'='*60}")
            print(f"Critical Liquidation Zones - {leverage} Leverage")
            print(f"{'='*60}")
            print(critical_zones.to_string(index=False))
            print(f"{'='*60}\n")
            
            logger.info("Critical zones identified successfully")
            
        except Exception as e:
            logger.error(f"Error identifying critical zones: {str(e)}")
    
    def create_interactive_heatmap(
        self,
        leverage: str = "100x",
        save_path: Optional[str] = None
    ) -> None:
        """Create interactive Plotly heatmap"""
        try:
            df = self.processor.get_leverage_data(leverage)
            
            fig = go.Figure()
            
            # Long liquidations
            long_df = df[df['position_type'] == 'Long']
            fig.add_trace(go.Bar(
                x=long_df['liq_price'],
                y=long_df['liq_level'],
                name='Long Liquidations',
                marker_color='red',
                opacity=0.6,
                hovertemplate='<b>Price:</b> $%{x:,.0f}<br>' +
                             '<b>Amount:</b> $%{y:,.0f}<br>' +
                             '<extra></extra>'
            ))
            
            # Short liquidations
            short_df = df[df['position_type'] == 'Short']
            fig.add_trace(go.Bar(
                x=short_df['liq_price'],
                y=short_df['liq_level'],
                name='Short Liquidations',
                marker_color='green',
                opacity=0.6,
                hovertemplate='<b>Price:</b> $%{x:,.0f}<br>' +
                             '<b>Amount:</b> $%{y:,.0f}<br>' +
                             '<extra></extra>'
            ))
            
            # Current price line
            fig.add_vline(
                x=self.current_price,
                line_dash="dash",
                line_color="blue",
                line_width=2,
                annotation_text=f"Current: ${self.current_price:,.0f}",
                annotation_position="top"
            )
            
            fig.update_layout(
                title=f'Interactive Liquidation Heatmap - {leverage} Leverage',
                xaxis_title='Price (USD)',
                yaxis_title='Liquidation Amount (USD)',
                hovermode='x unified',
                template='plotly_dark',
                height=600
            )
            
            if save_path:
                fig.write_html(save_path)
            
            fig.show()
            
            logger.info("Interactive heatmap created successfully")
            
        except Exception as e:
            logger.error(f"Error creating interactive heatmap: {str(e)}")
