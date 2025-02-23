import ccxt
import os
from .chart_data_provider import ChartDataProvider # Changed to relative import

class BinanceDataProvider(ChartDataProvider):
    """
    Component for fetching chart data from Binance exchange.
    """

    def __init__(self, config):
        super().__init__(config)
        self.api_key = config.get("BINANCE_API_KEY")
        self.api_secret = config.get("BINANCE_SECRET_KEY")
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
    def get_ticker(self, symbol, market_type='spot'):
        """
        Fetches ticker data for a specific symbol from Binance.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTC/USDT').
            market_type (str, optional): 'spot' or 'futures'. Defaults to 'spot'.

        Returns:
            dict: Ticker data for the symbol.
        """
        try:
            if market_type == 'futures':
                ticker = self.exchange_client.fetch_ticker(symbol) # Use just symbol for futures
            else:
                ticker = self.exchange_client.fetch_ticker(symbol) # For spot market
            return ticker
        except Exception as e:
            print(f"Error fetching ticker for {symbol} ({market_type}) from Binance: {e}")
            return None

    def place_order(self, symbol, side, quantity, market_type='spot', order_type='market'):
        """
        Places an order on Binance.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTC/USDT').
            side (str): 'buy' or 'sell'.
            quantity (float): The quantity to trade.
            market_type (str, optional): 'spot' or 'futures'. Defaults to 'spot'.
            order_type (str, optional): 'market' or 'limit'. Defaults to 'market'.

        Returns:
            dict: Order details from exchange or None if error.
        """
        try:
            if market_type == 'futures':
                order = self.exchange_client.create_order(
                    symbol=symbol, # Use just symbol for futures order
                    type=order_type,
                    side=side,
                    amount=quantity,
                )
            else: # Spot market
                order = self.exchange_client.create_order(
                    symbol=symbol,
                    type=order_type,
                    side=side,
                    amount=quantity,
                )
            return order
        except Exception as e:
            print(f"Error placing {order_type} {side} order for {quantity} {symbol} ({market_type}) on Binance: {e}")
            return None
