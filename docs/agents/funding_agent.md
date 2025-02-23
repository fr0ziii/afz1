# Funding Agent

## Description

The Funding Agent is designed for monitoring and analyzing funding rate data in cryptocurrency markets. It provides a basic framework for agents that can track funding rates, identify trends, and potentially generate signals based on funding rate analysis. This agent can be valuable for traders interested in incorporating funding rates into their trading strategies, particularly in perpetual futures markets.

## Missions

[Description of the missions this agent is designed to accomplish. Link to mission files if applicable.]
- Currently, no specific mission files are defined for the Funding Agent. Missions would be defined based on the specific funding rate analysis tasks and signal generation strategies it is intended to handle.

## Configuration

The Funding Agent can be configured with the following parameters in the `agent_config` section of the main configuration:

-   **agent_id**: A unique identifier for the agent instance (inherited from `BaseAgent`).
-   **agent_type**: Must be set to `FundingAgent` (inherited from `BaseAgent`).
-   **trading_pairs**: A list of trading pairs to monitor for funding rate arbitrage opportunities (e.g., `["BTCUSDT", "ETHUSDT"]`). Defaults to `["BTCUSDT", "ETHUSDT"]`.
-   **funding_rate_threshold**: The funding rate threshold (as a decimal, e.g., `0.0001` for 0.01%) above which arbitrage opportunities are considered. Defaults to `0.0001` (0.01%).
-   **slippage_tolerance**: The maximum allowed slippage (as a decimal, e.g., `0.001` for 0.1%) for spot market orders during arbitrage execution. Defaults to `0.001` (0.1%).
-   **spot_order_type**: The order type to use for spot market orders in arbitrage trades (e.g., `"market"`, `"limit"`). Defaults to `"market"`.

### Example Configuration

```yaml
config:
  agent_id: funding_agent_01
  agent_type: FundingAgent
  agent_config:
    binance_api: # Binance API configuration (required for BinanceDataProvider)
      api_key: "YOUR_BINANCE_API_KEY"
      api_secret: "YOUR_BINANCE_API_SECRET"
    trading_pairs: ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    funding_rate_threshold: 0.0002  # 0.02% threshold
    slippage_tolerance: 0.0005     # 0.05% slippage tolerance
    spot_order_type: "market"
```

## Inputs and Outputs

### Inputs

-   **Funding Rate Data**: Real-time or historical funding rate data from cryptocurrency exchanges.
-   **Trading Pair Information**:  List of trading pairs for which funding rates should be monitored.

### Outputs

-   **Funding Rate Alerts**: Alerts triggered when funding rates meet certain criteria (e.g., exceed thresholds, trend changes).
-   **Funding Rate Analysis**:  Analysis of funding rate data, potentially including trends, historical comparisons, and visualizations (future implementation).
-   **Logs**: Informational and error logs for monitoring agent activity and debugging.

## Workflow

1.  **Fetch Funding Rate Data**: The agent fetches funding rate data for configured trading pairs from cryptocurrency exchanges (currently placeholder logic).
2.  **Analyze Funding Rates**: The agent analyzes the fetched funding rate data, looking for trends or conditions based on configured parameters (currently placeholder logic).
3.  **Generate Alerts**: The agent generates alerts when funding rates meet predefined criteria (currently placeholder logic).
4.  **Output Analysis**:  In future implementations, the agent can output more detailed analysis of funding rate data.
5.  **Log Activity**: The agent logs funding rate monitoring activities, analysis results, and generated alerts for monitoring and analysis.

## Example Usage

To run the Funding Agent, you would instantiate and run the agent, configuring it with data sources and trading pairs to monitor. Since the current implementation is basic, the example usage primarily involves setting up the agent and potentially adding funding rate monitoring logic.

```python
from src.agents.funding_agent import FundingAgent

config = {
  "agent_id": "funding_agent_01",
  "agent_type": "FundingAgent",
}

agent = FundingAgent(config)
# agent.run() # Run method currently placeholder
# Example of configuring trading pairs to monitor (to be implemented)
# config["trading_pairs"] = ["BTC/USDT", "ETH/USDT"]
# agent = FundingAgent(config)
# agent.start_monitoring_funding_rates() # Method to initiate funding rate monitoring (to be implemented)
```

This example shows the basic instantiation of the Funding Agent. The `run` method is currently a placeholder and would need to be implemented with actual funding rate monitoring logic. Future implementations would include methods to configure trading pairs and initiate monitoring.

## Code Location

-   `src/agents/funding_agent.py`

## Components

-   **`src/agents/base_agent.py` (BaseAgent)**: The Funding Agent inherits basic agent functionalities from the `BaseAgent`.
-   **Funding Rate Data Components (To be implemented)**: Future implementations would include components for fetching funding rate data from various cryptocurrency exchanges (e.g., API integrations).
-   **Funding Rate Analysis Components (Future)**: Components for analyzing funding rate data, detecting trends, and generating insights.
-   **Alerting Components (Future)**: Components for generating and delivering alerts based on funding rate conditions.

## Notes and Considerations

-   **Debugging and Progress**: Significant debugging and fixes have been implemented to get the `FundingAgent` to fetch funding rates, identify arbitrage opportunities, fetch ticker data, and attempt to place orders.
-   **Implemented `get_ticker` and `place_order`**: The `get_ticker` and `place_order` methods have been implemented in `BinanceDataProvider` to enable ticker data fetching and order placement functionalities.
-   **Symbol Format Fixes**: Symbol format issues for both ticker fetching and order placement with `binanceusdm` exchange client have been identified and resolved.
-   **Price Extraction Fix**: Price extraction logic in `_execute_arbitrage_trade` has been corrected to use `'last'` instead of `'lastPrice'` to align with the ticker data format.
-   **API Key Requirement**: The agent now requires Binance API keys to be set as environment variables (`BINANCE_API_KEY` and `BINANCE_API_SECRET`) for order placement to function.
-   **Next Steps**: The next step is to set the Binance API keys and test the order placement functionality of the `FundingAgent`.
-   **Further Enhancements**: Future enhancements include implementing actual trade execution logic, slippage control, order type configurations, and comprehensive testing on Binance Testnet.
-   **Data Source Integration**:  Further data source integration and analysis logic can be added to enhance the agent's capabilities.
-   **Alerting Mechanisms**:  Implementing alerting mechanisms to notify users when arbitrage opportunities are identified or trades are executed.
-   **Backtesting and Validation**:  Backtest and validate the arbitrage strategy and trading logic to ensure their effectiveness before deploying in live trading scenarios.