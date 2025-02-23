import asyncio
import aiohttp
import websockets
import json
import logging # Replace structlog with basic logging
from sortedcontainers import SortedDict # Import SortedDict

class MyOrderBookFetcher: # Renamed class to MyOrderBookFetcher
    """
    Fetches real-time order book data from Binance API and manages order book using SortedDict.
    """
    def __init__(self, trading_pair: str = "BTCUSDT"):
        self.trading_pair = trading_pair.upper()
        # self.logger = structlog.get_logger(__name__) # Removed structlog
        self.logger = logging.getLogger(__name__) # Use basic logging
        self.logger.setLevel(logging.DEBUG) # Set logger level to DEBUG in OrderBookFetcher
        self.logger.debug("OrderBookFetcher logger initialized in __init__") # Debug log in __init__
        self.websocket_url = f"wss://stream.binance.com:9443/ws/{self.trading_pair.lower()}@depth@100ms"
        self.rest_snapshot_url = f"https://api.binance.com/api/v3/depth?symbol={self.trading_pair}&limit=100"
        self.session = None  # aiohttp session for REST requests
        self.ws = None       # websocket connection
        self.bids = SortedDict() # Use SortedDict for bids
        self.asks = SortedDict() # Use SortedDict for asks

        async def initialize_session(self):
            """
            Initializes aiohttp session for REST requests.
            """
            if not self.session:
                self.session = aiohttp.ClientSession()

        async def fetch_orderbook_snapshot(self):
            """
            Fetches order book snapshot from Binance REST API.
            """
            await self.initialize_session()
            try:
                async with self.session.get(self.rest_snapshot_url) as response:
                    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                    return await response.json()
            except aiohttp.ClientError as e:
                self.logger.error("Error fetching orderbook snapshot from REST API.", error=str(e))
                return None

        async def connect_websocket(self):
            """
            Connects to Binance WebSocket for order book updates.
            """
            try:
                self.ws = await websockets.connect(self.websocket_url)
                self.logger.info(f"WebSocket connected to {self.websocket_url}")
            except websockets.exceptions.ConnectionClosed as e:
                self.logger.error("WebSocket connection closed unexpectedly.", error=str(e))
                return False
            except Exception as e:  # Catching broad exception for initial connection errors
                self.logger.error("Error connecting to WebSocket.", error=str(e))
                return False
            return True

        async def receive_messages(self):
            """
            Receives and processes WebSocket messages.
            """
            if self.ws is None:  # Reconnect if websocket is None
                if not await self.connect_websocket():
                    return

            try:
                async for message in self.ws:
                    order_book_update = json.loads(message)
                    
                    # Update bids and asks using SortedDict
                    for bid_update in order_book_update.get('b', []):
                        price = float(bid_update[0])
                        size = float(bid_update[1])
                        if size == 0:
                            if price in self.bids:
                                del self.bids[price] # Remove bid if size is 0
                        else:
                            self.bids[price] = size  # Update bid price with new size

                    for ask_update in order_book_update.get('a', []):
                        price = float(ask_update[0])
                        size = float(ask_update[1])
                        if size == 0:
                            if price in self.asks:
                                del self.asks[price] # Remove ask if size is 0
                        else:
                            self.asks[price] = size  # Update ask price with new size


                    # Log essential details from the update
                    self.logger.debug(
                        "Order book update processed.",
                        last_update_id=order_book_update.get('u'),
                        event_type=order_book_update.get('e'),
                        event_time=order_book_update.get('E'),
                        bids_count=len(order_book_update.get('b', [])),
                        asks_count=len(order_book_update.get('a', [])),
                        bids_depth=len(self.bids), # Log current bids depth
                        asks_depth=len(self.asks), # Log current asks depth
                    )
                    self.logger.debug(f"Order book Bids depth: {len(self.bids)}, Asks depth: {len(self.asks)}") # Added debug log to check SortedDict updates
                    # In a real implementation, process and queue the updates

            except websockets.exceptions.ConnectionClosed as e:
                self.logger.warning(f"WebSocket connection closed: {e}")
                # Reconnection logic is handled in run_forever loop
            except Exception as e:
                self.logger.error(f"Error receiving message: {e}", exc_info=True)
            # finally block removed - no need to close ws here, let run_forever handle reconnect


            async def close_session(self):
                """
                Closes the aiohttp session.
                """
                if self.session:
                    await self.session.close()
                    self.session = None


            async def run_forever(self):
                """
                Runs the websocket message receiver loop indefinitely.
                """
                while True:
                    await self.receive_messages()
                    await asyncio.sleep(5) # Wait before attempting to reconnect


if __name__ == "__main__":
    async def main():
        fetcher = OrderBookFetcher()
        snapshot = await fetcher.fetch_orderbook_snapshot()
        if snapshot:
            print("Orderbook Snapshot Bids (first 5):")
            for bid in snapshot['bids'][:5]:
                print(bid)
            print("\nOrderbook Snapshot Asks (first 5):")
            for ask in snapshot['asks'][:5]:
                print(ask)

        if await fetcher.connect_websocket():
            await fetcher.run_forever() # Run websocket listener in the background

        await fetcher.close_session()

    asyncio.run(main())
