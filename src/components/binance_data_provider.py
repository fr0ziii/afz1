import ccxt
from .chart_data_provider import ChartDataProvider # Changed to relative import

class BinanceDataProvider(ChartDataProvider):
    """
    Component for fetching chart data from Binance exchange.
    """

    def __init__(self, config):
        super().__init__(config)
        self.exchange_client = self.setup_exchange_client()

    def setup_exchange_client(self):
        """
        Sets up the Binance exchange client using ccxt library.
        """
        exchange = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
        })
        return exchange

    def fetch_data(self):
        """
        Fetches chart data from Binance API.
        """
        try:
            ohlcv = self.exchange_client.fetch_ohlcv(
                self.trading_pair,
                timeframe=self.timeframe,
                limit=100  # Fetch last 100 candles for example
            )
            return ohlcv
        except Exception as e:
            print(f"Error fetching data from Binance: {e}")
            return None