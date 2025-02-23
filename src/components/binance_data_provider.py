import ccxt
import os
from .chart_data_provider import ChartDataProvider # Changed to relative import

class BinanceDataProvider(ChartDataProvider):
    """
    Component for fetching chart data from Binance exchange.
    """

    def __init__(self, config):
        super().__init__(config)
        self.api_key = os.environ.get('BINANCE_API_KEY')
        self.api_secret = os.environ.get('BINANCE_SECRET_KEY')
        self.exchange_client = self.setup_exchange_client()

    def setup_exchange_client(self):
        """
        Sets up the Binance exchange client using ccxt library for USD-M futures.
        """
        exchange = ccxt.binanceusdm({ # Use binanceusdm for USD-M futures
            'apiKey': self.api_key, # Read API key from environment variable
            'secret': self.api_secret, # Read secret key from env variable
            'enableRateLimit': True, # Enable rate limiting
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

    def get_funding_rate(self, symbol):
        """
        Fetches funding rate for a specific symbol from Binance USD-M futures.
        """
        try:
            funding_rate = self.exchange_client.fetch_funding_rate(symbol) # Use unified symbol format
            return funding_rate
        except Exception as e:
            print(f"Error fetching funding rate for {symbol} from Binance: {e}")
            return None