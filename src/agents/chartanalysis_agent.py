import logging
from src.agents.base_agent import BaseAgent
from src.components.binance_data_provider import BinanceDataProvider
from src.components.pattern_recognizer import PatternRecognizer
from src.components.signal_generator import SignalGenerator
from src.components.technical_indicator_calculator import TechnicalIndicatorCalculator
from typing import Dict, List, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.config_manager import ConfigManager  # Import ConfigManager for type hinting

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChartAnalysisAgent(BaseAgent):
    """
    Agent for performing technical analysis on cryptocurrency charts.
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.config: Dict[str, Any] = self.load_config(config) # Load config using BaseAgent's method
        self.validate_config() # Validate configuration after loading
        self.chart_data_provider: BinanceDataProvider = self.setup_chart_data_provider()
        self.indicator_calculator: TechnicalIndicatorCalculator = self.setup_indicator_calculator()
        self.pattern_recognizer: PatternRecognizer = self.setup_pattern_recognizer()
        self.signal_generator: SignalGenerator = self.setup_signal_generator()
        self.config_manager: Dict[str, Any] = self.setup_config_manager() # Assuming config manager returns a dict for now

    def setup_dependencies(self) -> None:
        """
        Set up agent dependencies (currently empty).
        """
        pass # Add actual dependency setup later

    def setup_config_manager(self) -> Dict[str, Any]: # Assuming it returns a dict
        """
        Sets up the configuration manager component.
        For now, it will simply return the loaded config.
        In future, it can be extended to handle dynamic config updates etc.
        """
        return self.config

    def setup_chart_data_provider(self) -> BinanceDataProvider:
        """
        Sets up the chart data provider component.
        """
        return BinanceDataProvider(self.config)

    def setup_indicator_calculator(self) -> TechnicalIndicatorCalculator:
        """
        Sets up the technical indicator calculator component.
        """
        return TechnicalIndicatorCalculator(self.config)

    def setup_pattern_recognizer(self) -> PatternRecognizer:
        """
        Sets up the chart pattern recognizer component.
        """
        return PatternRecognizer(self.config)

    def setup_signal_generator(self) -> SignalGenerator:
        """
        Sets up the signal generator component.
        """
        logger.info("Signal generator setup") # Placeholder setup
        return SignalGenerator(self.config)

    def validate_config(self) -> None:
        """
        Validates the agent configuration to ensure required parameters are present and valid.
        """
        required_params = ["trading_pair", "timeframe", "indicators", "exchange"]
        for param in required_params:
            if param not in self.config:
                raise ValueError(f"Configuration parameter '{param}' is required.")
        if not isinstance(self.config["trading_pair"], str):
            raise TypeError("Configuration parameter 'trading_pair' must be a string.")
        if not isinstance(self.config["timeframe"], str):
            raise TypeError("Configuration parameter 'timeframe' must be a string.")
        if not isinstance(self.config["indicators"], list):
            raise TypeError("Configuration parameter 'indicators' must be a list.")
        if not isinstance(self.config["exchange"], str):
            raise TypeError("Configuration parameter 'exchange' must be a string.")


    def run(self) -> None:
        """
        Runs the chart analysis agent.
        """
        try:
            chart_data = self.chart_data_provider.fetch_data()  # Fetch data using data provider
            if chart_data:
                try:
                    indicator_df = self.indicator_calculator.calculate_indicators(chart_data)  # Calculate indicators
                    logger.info("Chart Data with Indicators:")
                    logger.info(indicator_df)
                except Exception as e:
                    logger.error(f"Error calculating indicators: {e}")
                    return

                try:
                    patterns = self.pattern_recognizer.recognize_patterns(chart_data)  # Recognize patterns
                    logger.info("\nRecognized Patterns:")
                    if patterns.get('doji'):
                        logger.info("Doji pattern detected.")
                    else:
                        logger.info("No Doji pattern detected.")
                except Exception as e:
                    logger.error(f"Error recognizing patterns: {e}")
                    return

                try:
                    signals = self.signal_generator.generate_signals(indicator_df, patterns)  # Generate signals
                    logger.info("\nTrading Signals:")
                    logger.info(signals)
                except Exception as e:
                    logger.error(f"Error generating signals: {e}")
                    return
            else:
                logger.info("Failed to fetch chart data.")
        except Exception as e:
            logger.error(f"Error fetching chart data: {e}")


    def stop(self) -> None:
        """
        Stops the chart analysis agent.
        """
        pass

if __name__ == "__main__":
    # Example usage (for testing purposes)
    config = {
        "agent_id": "chart_analysis_agent_01",
        "agent_type": "ChartAnalysisAgent",
        "data_source": "binance",
        "exchange": "Binance", # Added exchange to config
        "trading_pair": "XRP/USDT",
        "timeframe": "5m",
        "indicators": ["SMA", "EMA", "RSI", "MACD", "Bollinger Bands"], # Added indicators to config
        "indicator_periods": { # Corrected indicator periods config - RSI is now integer
            "SMA": [20, 50],
            "EMA": [20, 50],
            "RSI": 14, # RSI period as integer, not list
            "MACD": {"fast_period": 12, "slow_period": 26, "signal_period": 9}
        },
        "patterns": ["TrendLines", "SupportResistance", "Triangles"],
        # API keys can be added to config or environment variables
        # "api_key": "YOUR_BINANCE_API_KEY",
        # "api_secret": "YOUR_BINANCE_API_SECRET",
    }
    agent = ChartAnalysisAgent(config)
    agent.run()