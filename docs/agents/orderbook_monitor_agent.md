# Order Book Monitor Agent

## Description

The Order Book Monitor Agent is designed to monitor the Binance order book for a specific trading pair and detect large orders, defined by a USD value threshold. It fetches real-time order book data and current price from the Binance API, analyzes the order book to identify orders exceeding the threshold, and triggers alerts when large orders are detected. This agent is valuable for traders who want to monitor order book activity for significant buy or sell orders that could indicate potential market movements.

## Missions

[Description of the missions this agent is designed to accomplish. Link to mission files if applicable.]
- Currently, no specific mission files are defined for the Order Book Monitor Agent. Missions would be defined based on the specific monitoring parameters and alert triggers it is intended to handle.

## Configuration

The Order Book Monitor Agent is configured primarily through environment variables, loaded using `dotenv`. The following configuration parameters are available:

-   **agent_id**: A unique identifier for the agent instance.
-   **agent_type**: Must be set to `OrderBookMonitorAgent`.
-   **TRADING_PAIR** (Environment Variable): The trading pair to monitor on Binance (e.g., `BTCUSDT`, `XRPUSDT`). Defaults to `XRPUSDT`.
-   **LARGE_ORDER_THRESHOLD_USD** (Environment Variable): The USD value threshold for identifying large orders. Orders with a value equal to or exceeding this threshold will trigger alerts. Defaults to `1000000.0` (USD 1 million).
-   **MONITOR_INTERVAL** (Environment Variable): The interval in seconds between each order book data fetch and analysis cycle. Defaults to `10` seconds.

### Example Configuration (.env file)

Create a `.env` file in the project root directory with the following content to configure the agent:

```env
TRADING_PAIR=BTCUSDT
LARGE_ORDER_THRESHOLD_USD=5000000.0 # Set threshold to USD 5 million
MONITOR_INTERVAL=5             # Set monitor interval to 5 seconds
```

## Inputs and Outputs

### Inputs

-   **Binance Order Book Data**: Real-time order book data fetched from the Binance API for the configured `TRADING_PAIR`.
-   **Binance Current Price**: Real-time price data fetched from the Binance API for the configured `TRADING_PAIR`.
-   **Configuration Parameters**: Configuration loaded from environment variables, as described in the Configuration section.

### Outputs

-   **Alerts**: Real-time alerts printed to the console when large orders (exceeding `LARGE_ORDER_THRESHOLD_USD`) are detected in the order book. Alerts include order type (bid/ask), quantity, price, and USD value.
-   **Console Output**:  Prints agent status messages, current price updates, and error messages to the console.
-   **Logs**: (Implicit) Prints informational and error messages to the console, which can be considered basic logging. For more robust logging, the agent would need to be extended.

## Workflow

1.  **Load Configuration**: The agent loads configuration parameters from environment variables using `ConfigurationManager`.
2.  **Initialize Components**: The agent initializes `OrderBookFetcher`, `PriceFetcher`, `OrderBookAnalyzer`, and `AlertManager` components, using the loaded configuration.
3.  **Fetch Data**: In a continuous loop, the agent fetches order book data and current price for the configured trading pair from Binance API using `OrderBookFetcher` and `PriceFetcher`.
4.  **Analyze Order Book**: The agent uses `OrderBookAnalyzer` to analyze the fetched order book data for large orders (bids or asks) that exceed the configured `LARGE_ORDER_THRESHOLD_USD`.
5.  **Trigger Alerts**: When large orders are detected, the agent uses `AlertManager` to trigger alerts, printing messages to the console.
6.  **Wait and Repeat**: The agent waits for the duration specified by `MONITOR_INTERVAL` and repeats steps 3-5.
7.  **Stop**: The agent can be stopped by sending a KeyboardInterrupt signal (e.g., Ctrl+C), which gracefully stops the monitoring loop.

## Example Usage

1.  **Configure Environment Variables**: Create a `.env` file in the project root and set the desired configuration parameters (e.g., `TRADING_PAIR`, `LARGE_ORDER_THRESHOLD_USD`, `MONITOR_INTERVAL`).
2.  **Run the Agent**: Execute the agent script directly from the command line:

    ```bash
    python src/agents/orderbook_monitor_agent.py
    ```

    The agent will start monitoring the order book and print alerts to the console when large orders are detected.
3.  **Stop the Agent**: Press `Ctrl+C` in the terminal to stop the agent gracefully.

## Code Location

-   `src/agents/orderbook_monitor_agent.py`

## Components

-   **`src/agents/base_agent.py` (BaseAgent)**: (Simplified BaseAgent included in the same file): Provides a basic agent class with status management.
-   **`OrderBookFetcher`**: Fetches order book data from the Binance API for a given trading pair.
-   **`PriceFetcher`**: Fetches the current price of a trading pair in USD from the Binance API.
-   **`OrderBookAnalyzer`**: Analyzes order book data to identify large orders (bids or asks) exceeding a USD value threshold.
-   **`AlertManager`**: Manages alert notifications. In the current implementation, it simply prints alerts to the console.
-   **`ConfigurationManager`**: Loads configuration parameters from environment variables.

## Notes and Considerations

-   **Environment Configuration**: The agent relies heavily on environment variables for configuration. Ensure that `.env` file is correctly configured with the desired settings.
-   **API Rate Limits**: The agent fetches data from Binance API. Be mindful of Binance API rate limits. Adjust `MONITOR_INTERVAL` if necessary to avoid hitting rate limits.
-   **Error Handling**: The agent includes basic error handling for API requests, but more robust error handling and logging mechanisms could be implemented for production use.
-   **Alerting Enhancements**: The `AlertManager` currently only prints alerts to the console. This can be extended to support more sophisticated alerting methods (e.g., email, push notifications, webhooks).
-   **USD Threshold**: The large order threshold is defined in USD value (`LARGE_ORDER_THRESHOLD_USD`). Ensure this threshold is appropriate for the trading pair being monitored and the intended use case.
-   **Trading Pair**: The agent is designed to monitor a single trading pair, configured by the `TRADING_PAIR` environment variable. To monitor multiple trading pairs, multiple instances of the agent would need to be run.