class ChartDataProvider:
    """
    Component for fetching chart data from various data sources.
    """

    def __init__(self, config):
        self.config = config
        self.data_source = self.config.get("data_source", "binance") # Default to binance
        self.exchange = self.config.get("exchange", "Binance") # Default to Binance
        self.trading_pair = self.config.get("trading_pair", "BTC/USDT") # Default to BTC/USDT
        self.timeframe = self.config.get("timeframe", "1h") # Default to 1h
        self.api_key = self.config.get("api_key")
        self.api_secret = self.config.get("api_secret")

    def fetch_data(self):
        """
        Fetches chart data from the specified data source.
        This method should be implemented by subclasses for specific data sources.
        """
        raise NotImplementedError("Subclasses must implement fetch_data method")