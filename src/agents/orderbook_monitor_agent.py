import requests
import time
from dotenv import load_dotenv
import os

# BaseAgent class (simplified for this example)
class BaseAgent:
    def __init__(self, config=None):
        self.config = config or {}
        self.status = "initialized"

    def _set_status(self, status):
        self.status = status

class OrderBookFetcher:
    """Fetches order book data from Binance API."""
    def __init__(self, trading_pair):
        self.endpoint = "https://api.binance.com/api/v3/depth"
        self.trading_pair = trading_pair

    def fetch_order_book(self):
        """Returns order book data or None if an error occurs."""
        params = {"symbol": self.trading_pair}
        try:
            response = requests.get(self.endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching order book: {e}")
            return None

class PriceFetcher:
    """Fetches the current price of the asset in USD."""
    def __init__(self, trading_pair):
        self.endpoint = "https://api.binance.com/api/v3/ticker/price"
        self.trading_pair = trading_pair

    def fetch_current_price(self):
        """Returns the current price as a float or None if an error occurs."""
        params = {"symbol": self.trading_pair}
        try:
            response = requests.get(self.endpoint, params=params)
            response.raise_for_status()
            return float(response.json()["price"])
        except (requests.exceptions.RequestException, KeyError, ValueError) as e:
            print(f"Error fetching price: {e}")
            return None

class OrderBookAnalyzer:
    """Analyzes order book data for large orders based on USD value."""
    def __init__(self, large_order_threshold_usd):
        self.threshold_usd = large_order_threshold_usd

    def analyze_order_book(self, order_book_data, current_price):
        """Returns a list of orders exceeding the USD threshold."""
        if not order_book_data or current_price is None:
            return []
        large_orders = []
        # Analyze bids
        for bid in order_book_data.get("bids", []):
            price, quantity = float(bid[0]), float(bid[1])
            value_usd = price * quantity
            if value_usd >= self.threshold_usd:
                large_orders.append({"type": "bid", "price": price, "quantity": quantity, "value_usd": value_usd})
        # Analyze asks
        for ask in order_book_data.get("asks", []):
            price, quantity = float(ask[0]), float(ask[1])
            value_usd = price * quantity
            if value_usd >= self.threshold_usd:
                large_orders.append({"type": "ask", "price": price, "quantity": quantity, "value_usd": value_usd})
        return large_orders

    def calculate_buy_sell_ratio(self, large_orders):
        """Calculates the buy/sell ratio of large orders."""
        if not large_orders:
            return 0.5  # Default to neutral if no large orders
        buy_orders = sum(1 for order in large_orders if order["type"] == "bid")
        sell_orders = sum(1 for order in large_orders if order["type"] == "ask")
        total_orders = buy_orders + sell_orders
        if total_orders == 0:
            return 0.5  # Default to neutral if no large orders
        return buy_orders / total_orders

def identify_support_resistance_levels(self, large_orders, top_levels=3):
    """Identifies support and resistance levels based on large order concentration."""
    if not large_orders:
        return []
    price_levels = {}
    for order in large_orders:
        price = order["price"]
        price_levels[price] = price_levels.get(price, 0) + 1
    sorted_levels = sorted(price_levels.items(), key=lambda item: item[1], reverse=True)
    top_levels_prices = [level[0] for level in sorted_levels[:top_levels]]
    return top_levels_prices

class AlertManager:
    """Handles alert notifications."""
    def trigger_alert(self, message):
        """Prints the alert message (extendable to other methods)."""
        print(f"ALERT: {message}")

class ConfigurationManager:
    """Loads configuration settings."""
    def __init__(self):
        load_dotenv()
        self.trading_pair = os.getenv("TRADING_PAIR", "XRPUSDT")
        self.large_order_threshold_usd = float(os.getenv("LARGE_ORDER_THRESHOLD_USD", 1000000.0))  # $1M default
        self.monitor_interval = int(os.getenv("MONITOR_INTERVAL", 10))  # 10s default

    def load_configuration(self):
        """Returns configuration as a dictionary."""
        return {
            "trading_pair": self.trading_pair,
            "large_order_threshold_usd": self.large_order_threshold_usd,
            "monitor_interval": self.monitor_interval
        }

class OrderBookMonitorAgent(BaseAgent):
    """Monitors the order book and alerts on large orders (> $1M)."""
    def __init__(self, name="OrderBookMonitorAgent", config=None):
        super().__init__(config=config)
        self.name = name
        self.config_manager = ConfigurationManager()
        self.config = self.config_manager.load_configuration()
        self.trading_pair = self.config["trading_pair"]
        self.order_book_fetcher = OrderBookFetcher(self.trading_pair)
        self.price_fetcher = PriceFetcher(self.trading_pair)
        self.order_book_analyzer = OrderBookAnalyzer(self.config["large_order_threshold_usd"])
        self.alert_manager = AlertManager()
        self.monitor_interval = self.config["monitor_interval"]
        self.running = True

    def run(self):
        """Continuously monitors the order book."""
        self._set_status("running")
        print(f"{self.name} monitoring {self.trading_pair}...")
        while self.running:
            order_book_data = self.order_book_fetcher.fetch_order_book()
            current_price = self.price_fetcher.fetch_current_price()
            print(f"Current price: {current_price}")
            if order_book_data and current_price:
                large_orders = self.order_book_analyzer.analyze_order_book(order_book_data, current_price)
                if large_orders:
                    buy_sell_ratio = self.order_book_analyzer.calculate_buy_sell_ratio(large_orders)
                    ratio_percentage = buy_sell_ratio * 100
                    for order in large_orders:
                        message = f"Large {order['type']} detected: {order['quantity']} @ {order['price']} (Value: ${order['value_usd']:,.2f}). Buy/Sell Ratio: {ratio_percentage:.2f}%"
                        self.alert_manager.trigger_alert(message)
                else:
                    print(f"Failed to fetch data for {self.trading_pair}")
            time.sleep(self.monitor_interval)

    def stop(self):
        """Stops the agent."""
        self.running = False
        self._set_status("stopped")
        print(f"{self.name} stopped.")

if __name__ == "__main__":
    agent = OrderBookMonitorAgent()
    try:
        agent.run()
    except KeyboardInterrupt:
        agent.stop()