import logging
from src.agents.base_agent import BaseAgent
from src.components.binance_data_provider import BinanceDataProvider

logger = logging.getLogger(__name__)

class FundingAgent(BaseAgent):
    """
    Agent responsible for monitoring funding rates and identifying arbitrage opportunities.
    """

    def __init__(self, config, exchange_interface=None):
        """
        Initializes the FundingAgent.

        Args:
            config (dict): Configuration dictionary containing agent settings.
                agent_config (dict): Agent-specific configurations.
                    binance_api (dict): Binance API credentials (required).
                        api_key (str): Binance API key.
                        api_secret (str): Binance API secret.
                    trading_pairs (list): List of trading pairs to monitor.
                    funding_rate_threshold (float): Funding rate threshold for arbitrage.
                    slippage_tolerance (float): Slippage tolerance for spot orders.
                    spot_order_type (str): Order type for spot orders ('market', 'limit').
            exchange_interface (object, optional): Interface for interacting with the exchange.
        """
        super().__init__(config)
        self.exchange_interface = exchange_interface

        agent_config = config.get("agent_config", {})
        self.funding_rate_threshold = agent_config.get("funding_rate_threshold", 0.0001)  # Default 0.01%
        self.trading_pairs = agent_config.get("trading_pairs", ["BTCUSDT", "ETHUSDT"]) # Default pairs
        self.slippage_tolerance = agent_config.get("slippage_tolerance", 0.001) # Default 0.1%
        self.spot_order_type = agent_config.get("spot_order_type", "market") # Default to market order

        logger.info("FundingAgent initialized")

    def setup_dependencies(self):
        """
        Sets up dependencies for the agent, such as initializing the exchange interface.
        """
        print("FundingAgent setup_dependencies is being called...")
        logger.info("FundingAgent setup_dependencies called")
        super().setup_dependencies()
        agent_config = self.config.get("agent_config", {})
        self.exchange_interface = BinanceDataProvider(agent_config.get("binance_api", {}))
        logger.info(f"FundingAgent setup_dependencies: exchange_interface initialized: {self.exchange_interface}")

    def run(self):
        """
        Executes the main logic of the FundingAgent:
        1. Monitors funding rates.
        2. Identifies arbitrage opportunities.
        3. Executes trades based on opportunities.
        """
        logger.info("FundingAgent is running... - START")
        print("FundingAgent run method is executing...")
        # Monitor funding rates for trading pairs
        funding_rates = self._monitor_funding_rates()
        # Identify arbitrage opportunities based on funding rates
        opportunities = self._identify_arbitrage_opportunities(funding_rates)
        # Execute trades for each identified opportunity
        for opportunity in opportunities:
            self._execute_arbitrage_trade(opportunity)

    def _monitor_funding_rates(self):
        """
        Monitors funding rates for configured trading pairs.

        Returns:
            dict: A dictionary mapping trading pairs to their funding rate data.
        """
        print("FundingAgent _monitor_funding_rates is being called...")
        logger.info(f"FundingAgent _monitor_funding_rates: exchange_interface value: {self.exchange_interface}")
        trading_pairs = self.trading_pairs # Use configured trading pairs
        logger.info(f"Monitoring funding rates for trading pairs: {trading_pairs}")
        funding_rates = {}
        for pair in trading_pairs:
            logger.info(f"Fetching funding rate for {pair}...")
            try:
                rate_data = self.exchange_interface.get_funding_rate(pair)
                if rate_data:
                    funding_rates[pair] = rate_data
                    logger.info(f"Funding Rate for {pair}: {rate_data}")
                else:
                    logger.warning(f"Could not fetch funding rate for {pair}. Rate data is None.")
            except Exception as e:
                logger.error(f"Error fetching funding rate for {pair}: {e}", exc_info=True) # Capture full exception details
        return funding_rates

    def _identify_arbitrage_opportunities(self, funding_rates):
        """
        Identifies potential arbitrage opportunities based on funding rate discrepancies.

        Args:
            funding_rates (dict): A dictionary mapping trading pairs to their funding rate data.

        Returns:
            list: A list of dictionaries, each representing an arbitrage opportunity.
        """
        threshold = self.funding_rate_threshold
        opportunities = []
        for pair, rate_data in funding_rates.items():
            funding_rate = float(rate_data['fundingRate'])  # Extract funding rate from rate_data
            if abs(funding_rate) > threshold:
                # Determine trade direction based on funding rate sign
                direction = 'short_perp_buy_spot' if funding_rate > 0 else 'long_perp_short_spot'
                opportunities.append({
                    'pair': pair,
                    'direction': direction,
                    'funding_rate': funding_rate
                })
                logger.info(f"Arbitrage opportunity identified for {pair}: {direction}, funding rate: {funding_rate}")
        return opportunities

    def _execute_arbitrage_trade(self, opportunity):
        """
        Executes arbitrage trades to capitalize on funding rate differences.

        Args:
            opportunity (dict): A dictionary containing arbitrage opportunity details,
                               including pair, direction, and funding rate.
        """
        pair = opportunity['pair']
        direction = opportunity['direction']
        funding_rate = opportunity['funding_rate']
        logger.info(f"Executing arbitrage trade for {pair}: {direction}, funding rate: {funding_rate}")

        # Define position size in quote currency (e.g., USDT)
        position_size = 1000  # Fixed size for simplicity; adjust as needed

        # Get current prices for perpetual futures and spot markets
        try:
            perp_ticker = self.exchange_interface.get_ticker(pair, market_type='futures')
            spot_ticker = self.exchange_interface.get_ticker(pair, market_type='spot')
            perp_price = float(perp_ticker['lastPrice'])
            spot_price = float(spot_ticker['lastPrice'])
        except Exception as e:
            logger.error(f"Error fetching prices for {pair}: {e}")
            return

        # Calculate quantities to trade
        perp_quantity = position_size / perp_price  # Quantity for perpetual futures
        spot_quantity = position_size / spot_price  # Quantity for spot market

        try:
            if direction == 'short_perp_buy_spot':
                # Slippage check for spot buy order
                slippage = (spot_price - perp_price) / spot_price
                if slippage > self.slippage_tolerance:
                    logger.warning(f"Slippage too high for {pair} (short_perp_buy_spot): {slippage:.4f} > {self.slippage_tolerance:.4f}. Skipping trade.")
                    return
                # Short perpetual futures (receive funding when funding_rate > 0)
                self.exchange_interface.place_order(
                    pair, 'sell', perp_quantity, market_type='futures'
                )
                # Buy spot market to hedge
                self.exchange_interface.place_order(
                    pair, 'buy', spot_quantity, market_type='spot'
                )
            elif direction == 'long_perp_short_spot':
                # Slippage check for spot sell order
                slippage = (perp_price - spot_price) / spot_price
                if slippage > self.slippage_tolerance:
                    logger.warning(f"Slippage too high for {pair} (long_perp_short_spot): {slippage:.4f} > {self.slippage_tolerance:.4f}. Skipping trade.")
                    return
                # Long perpetual futures (receive funding when funding_rate < 0)
                self.exchange_interface.place_order(
                    pair, 'buy', perp_quantity, market_type='futures'
                )
                # Short spot market to hedge (assuming margin trading is enabled)
                self.exchange_interface.place_order(
                    pair, 'sell', spot_quantity, market_type='spot', order_type=self.spot_order_type
                )
            logger.info(f"Successfully executed arbitrage trade for {pair}: {direction}, spot_order_type: {self.spot_order_type}, slippage_tolerance: {self.slippage_tolerance}")
        except Exception as e:
            logger.error(f"Error executing arbitrage trade for {pair}: {direction}, spot_order_type: {self.spot_order_type}, slippage_tolerance: {self.slippage_tolerance}, error: {e}")

    def stop(self):
        """
        Stops the FundingAgent and any background processes.
        """
        logger.info("FundingAgent stop called")
        super().stop()
        # Add any FundingAgent-specific stop logic here, e.g., closing open positions

if __name__ == '__main__':
    # Example usage or testing
    config = {"trading_pairs": ["BTCUSDT", "ETHUSDT"], "agent_config": {"binance_api": {}}}
    agent = FundingAgent(config)
    agent.setup_dependencies()
    agent.run()