from src.agents.base_agent import BaseAgent # Changed to absolute import
from src.components.binance_data_provider import BinanceDataProvider # Changed to absolute import
from ..components.pattern_recognizer import PatternRecognizer # Import PatternRecognizer
from ..components.signal_generator import SignalGenerator # Import SignalGenerator
from src.components.technical_indicator_calculator import TechnicalIndicatorCalculator # Import TechnicalIndicatorCalculator

class ChartAnalysisAgent(BaseAgent):
    """
    Agent for performing technical analysis on cryptocurrency charts.
    """

    def __init__(self, config):
        super().__init__(config)
        self.config = self.load_config(config) # Load config using BaseAgent's method
        self.chart_data_provider = self.setup_chart_data_provider()
        self.indicator_calculator = self.setup_indicator_calculator()
        self.pattern_recognizer = self.setup_pattern_recognizer()
        self.signal_generator = self.setup_signal_generator()
        self.config_manager = self.setup_config_manager()

    def setup_dependencies(self):
        """
        Set up agent dependencies (currently empty).
        """
        pass # Add actual dependency setup later

    def setup_config_manager(self):
        """
        Sets up the configuration manager component.
        For now, it will simply return the loaded config.
        In future, it can be extended to handle dynamic config updates etc.
        """
        return self.config

    def setup_chart_data_provider(self):
        """
        Sets up the chart data provider component.
        """
        return BinanceDataProvider(self.config) # Instantiate BinanceDataProvider

    def setup_indicator_calculator(self):
        """
        Sets up the technical indicator calculator component.
        """
        return TechnicalIndicatorCalculator(self.config) # Instantiate TechnicalIndicatorCalculator

    def setup_pattern_recognizer(self):
        """
        Sets up the chart pattern recognizer component.
        """
        print("Pattern recognizer setup") # Placeholder setup
        return PatternRecognizer(self.config) # Instantiate PatternRecognizer

    def setup_signal_generator(self):
        """
        Sets up the signal generator component.
        """
        print("Signal generator setup") # Placeholder setup
        return SignalGenerator(self.config) # Instantiate SignalGenerator


    def run(self):
        """
        Runs the chart analysis agent.
        """
        chart_data = self.chart_data_provider.fetch_data() # Fetch data using data provider
        if chart_data:
            indicator_df = self.indicator_calculator.calculate_indicators(chart_data) # Calculate indicators
            print("Chart Data with Indicators:")
            print(indicator_df) # Print DataFrame with indicators

            patterns = self.pattern_recognizer.recognize_patterns(chart_data) # Recognize patterns
            print("\nRecognized Patterns:")
            print(patterns) # Print recognized patterns

            signals = self.signal_generator.generate_signals(indicator_df, patterns) # Generate signals
            print("\nTrading Signals:")
            print(signals) # Print trading signals
        else:
            print("Failed to fetch chart data.")


    def stop(self):
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
        "indicators": ["SMA", "EMA", "RSI", "MACD"], # Added indicators to config
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