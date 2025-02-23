from base_agent import BaseAgent
import requests  # For API calls
import os       # For environment variables
from dotenv import load_dotenv
from datetime import datetime
import time     # For sleep functionality

class WhaleWatcherAgent(BaseAgent):
    """
    Whale Watcher Agent for monitoring Ethereum blockchain for large transactions.
    """

    def __init__(self, config: dict):
        """Initialize the agent with API keys and state variables."""
        load_dotenv()  # Load environment variables from .env file
        super().__init__(config)
        self.etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
        if not self.etherscan_api_key:
            raise ValueError("ETHERSCAN_API_KEY environment variable is required")
        self.last_processed_block = None  # Track the last processed block
        self.running = True  # Control the run loop

    def run(self):
        """
        Execute the main whale watching logic in a continuous loop.
        """
        while self.running:
            print(f"🐳 Whale Watcher Agent running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            transactions, block_number = self._get_recent_transactions()
            if transactions is not None:
                eth_usd_price = self._get_eth_usd_price()
                if eth_usd_price:
                    whale_transactions = self._filter_whale_transactions(transactions, eth_usd_price)
                    if whale_transactions:
                        self._log_whale_transactions(whale_transactions)
                self.last_processed_block = block_number
            else:
                print("No new transactions to process.")
            time.sleep(3)  # Check every 3 seconds

    def stop(self):
        """
        Stop the whale watcher agent gracefully.
        """
        self.running = False
        print("Whale Watcher Agent stopping...")

    def _get_recent_transactions(self):
        """
        Fetch recent Ethereum transactions from Etherscan API.
        Returns a tuple (transactions, block_number) or (None, None) on failure/no new blocks.
        """
        etherscan_api_endpoint = "https://api.etherscan.io/api"
        try:
            # Get latest block number
            params = {
                "module": "proxy",
                "action": "eth_blockNumber",
                "apikey": self.etherscan_api_key,
            }
            response = requests.get(etherscan_api_endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            if "result" not in data:
                print(f"⚠️ Etherscan API error: {data.get('message', 'No result')}")
                return None, None
            latest_block_hex = data["result"]
            latest_block_number = int(latest_block_hex, 16)

            # Skip if no new block
            if self.last_processed_block is not None and latest_block_number <= self.last_processed_block:
                print(f"No new blocks since last check. Latest block: {latest_block_number}")
                return None, None

            # Get block with transactions
            params = {
                "module": "proxy",
                "action": "eth_getBlockByNumber",
                "tag": hex(latest_block_number),
                "boolean": "true",
                "apikey": self.etherscan_api_key,
            }
            response = requests.get(etherscan_api_endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            if "result" not in data or not data["result"]:
                print(f"⚠️ Etherscan API error: {data.get('message', 'No result')}")
                return None, None
            block = data["result"]
            block_timestamp = int(block["timestamp"], 16)  # Convert hex timestamp to int (seconds)
            transactions = block["transactions"]
            for tx in transactions:
                tx["timeStamp"] = block_timestamp  # Add block timestamp to each transaction
            return transactions, latest_block_number
        except requests.exceptions.RequestException as e:
            print(f"❌ Error connecting to Etherscan API: {e}")
            return None, None

    def _get_eth_usd_price(self):
        """
        Fetch current ETH-USD price from Binance API.
        """
        binance_api_endpoint = "https://api.binance.com/api/v3/ticker/price"
        params = {"symbol": "ETHUSDT"}
        try:
            response = requests.get(binance_api_endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            if "price" in data:
                eth_usd_price = float(data["price"])
                print(f"✅ Fetched ETH-USD price: ${eth_usd_price}")
                return eth_usd_price
            else:
                print("⚠️ Invalid response from Binance API")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching ETH-USD price: {e}")
            return None

    def _filter_whale_transactions(self, transactions, eth_usd_price):
        """
        Filter transactions to identify those exceeding $1,000,000 USD.
        """
        whale_transactions = []
        whale_threshold_usd = 1_000_000  # $1M threshold

        for tx in transactions:
            try:
                eth_value_wei = int(tx["value"], 16)  # Value in Wei (hex)
                eth_value = eth_value_wei / 10**18    # Convert to ETH
                usd_value = eth_value * eth_usd_price
                if usd_value >= whale_threshold_usd:
                    whale_transactions.append({
                        "hash": tx["hash"],
                        "timestamp": tx["timeStamp"],
                        "eth_value": eth_value,
                        "usd_value": usd_value,
                        "from_address": tx["from"],
                        "to_address": tx["to"]
                    })
            except (KeyError, ValueError, TypeError) as e:
                print(f"⚠️ Error processing tx {tx.get('hash', 'N/A')}: {e}")
                continue
        if whale_transactions:
            print(f"🐳 Found {len(whale_transactions)} whale transactions")
        return whale_transactions

    def _log_whale_transactions(self, whale_transactions):
        """
        Log details of whale transactions.
        """
        print("\n🐳 Whale Transactions Detected:")
        for tx in whale_transactions:
            timestamp_str = datetime.fromtimestamp(tx["timestamp"]).strftime('%Y-%m-%d %H:%M:%S')
            print("=" * 60)
            print(f"💰 Whale Transaction Alert")
            print(f"  Hash:        {tx['hash']}")
            print(f"  Value (USD): ${tx['usd_value']:,.2f}")
            print(f"  Value (ETH): {tx['eth_value']:.2f} ETH")
            print(f"  From:        {tx['from_address']}")
            print(f"  To:          {tx['to_address']}")
            print(f"  Timestamp:   {timestamp_str} (UTC)")
            print("=" * 60)

    def load_config(self, config: dict) -> dict:
        """Load and validate configuration."""
        return config

    def setup_dependencies(self):
        """Set up dependencies (currently empty)."""
        print("WhaleWatcherAgent dependencies setup...")
        pass

if __name__ == "__main__":
    config = {}
    agent = WhaleWatcherAgent(config)
    try:
        agent.run()
    except KeyboardInterrupt:
        agent.stop()