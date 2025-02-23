# Order Book Monitor Agent (`orderbook_monitor_agent.py`)

## Purpose

The Order Book Monitor Agent is designed to continuously monitor the order book activity for specific cryptocurrency trading pairs on Binance. By focusing on detecting and analyzing large orders, this agent aims to:

*   **Identify Potential Market Movers:** Large orders in the order book can often act as "icebergs" or hidden liquidity, and their presence or removal can signal potential shifts in market sentiment or price direction. The agent helps traders detect these potential market-moving events.
*   **Detect Support and Resistance Levels:**  Clusters of large orders at specific price levels can act as significant support or resistance zones. By monitoring order book depth and large order placements, the agent can assist in identifying these key levels.
*   **Anticipate Price Breakouts or Breakdowns:**  The appearance of large orders near price levels can sometimes indicate potential price breakouts (if buy orders accumulate above resistance) or breakdowns (if sell orders accumulate below support). The agent can provide early warnings of such potential events.
*   **Gain Insights into Market Depth and Liquidity:**  By continuously monitoring the order book and large order activity, the agent provides traders with a deeper understanding of market depth and liquidity for specific trading pairs on Binance.
*   **Trigger Real-time Trading Alerts:**  The agent's real-time alerting capabilities enable traders to receive immediate notifications when significant order book events occur, allowing for timely reaction to potential trading opportunities or risk events.

In essence, the Order Book Monitor Agent acts as a market surveillance tool, providing traders with valuable real-time insights into order book dynamics and potential market signals derived from large order activity on Binance.

## Functionality

The Order Book Monitor Agent provides the following core functionalities for real-time order book surveillance:

*   **Real-time Order Book Data Fetching:**
    - **Continuous Data Stream:** Establish and maintain a continuous data stream connection to the Binance exchange API to receive real-time order book updates for the configured trading pair.
    - **Efficient Data Handling:** Implement efficient data handling and parsing mechanisms to process high-frequency order book updates with minimal latency.
*   **Configurable Trading Pair Monitoring:**
    - **User-Defined Trading Pairs:** Allow users to configure the specific trading pairs (e.g., BTC/USDT, ETH/USDT) on Binance that the agent should monitor.
    - **Multiple Pair Monitoring:** (Future) Potentially extend the agent to monitor multiple trading pairs simultaneously, providing broader market surveillance capabilities.
*   **Large Order Detection and Filtering:**
    - **Threshold-Based Detection:** Implement logic to analyze the order book data and identify individual orders or clusters of orders that exceed a user-defined USD value threshold, classifying them as "large orders".
    - **Configurable Size Threshold:**  Allow users to easily configure the `LARGE_ORDER_THRESHOLD_USD` parameter via environment variables to customize the definition of "large orders" based on their trading preferences and risk tolerance.
*   **Real-time Alerting and Notifications:**
    - **Instant Console Alerts:**  Trigger real-time alerts directly to the console when large orders are detected, providing immediate visual notifications to the user.
    - **Detailed Alert Information:**  Include comprehensive information in each alert message, such as: Timestamp, Trading Pair, Order Side (BUY/SELL), Order Size (in base currency), Order Price, and USD Value of the order.
    - **Extendable Alerting Mechanisms:** (Future) Design the `AlertManager` component to be easily extensible to support additional alerting methods beyond console alerts, such as email notifications, Telegram messages, or webhook integrations to external platforms.
*   **Underlying Data Components and Utilities:**
    - **BinanceDataProvider:** Leverage the `BinanceDataProvider` component (or similar data provider) to handle Binance API interactions, data fetching, and data parsing efficiently.
    - **PriceFetcher Utility:** Utilize the `PriceFetcher` utility to fetch real-time price data for accurate USD value calculation of orders.
    - **OrderBookFetcher Utility:** Employ the `OrderBookFetcher` utility to encapsulate order book data fetching logic from the Binance API.
    - **ConfigurationManager Utility:** Utilize the `ConfigurationManager` component to handle agent configuration loading and parameter management, ensuring flexible and customizable agent behavior.

## AI Model(s) Used

The current implementation of the Order Book Monitor Agent relies on rule-based logic and threshold comparisons for large order detection and alerting, and does not directly utilize AI models. However, future versions of the agent could potentially benefit from AI in several ways:

*   **Advanced Order Book Pattern Recognition:**
    - **Machine Learning for Order Flow Analysis:**  Employ machine learning models (e.g., Recurrent Neural Networks, Convolutional Neural Networks) to analyze order book data and identify more complex patterns and signals beyond simple large order detection, such as order book imbalances, order flow dynamics, and spoofing/layering patterns.
    - **Dynamic Threshold Adjustment:**  Use AI-driven adaptive thresholding techniques to automatically adjust the `LARGE_ORDER_THRESHOLD_USD` parameter based on market volatility, trading volume, and historical order book patterns, optimizing the sensitivity and accuracy of large order detection.
*   **Predictive Alerting and Anomaly Detection:**
    - **Predictive Alerting Models:**  Train machine learning models to predict potential price movements or volatility spikes based on order book patterns and large order activity, enabling proactive alerting and early warnings for traders.
    - **Anomaly Detection for Unusual Order Book Activity:**  Utilize anomaly detection algorithms to identify unusual or statistically significant deviations in order book patterns or large order placements that may indicate market manipulation, flash crashes, or other anomalous events.
*   **Sentiment Analysis from Order Book Data:**
    - **Order Book Sentiment Scoring:**  Explore techniques to derive sentiment indicators directly from order book data, analyzing the ratio of buy vs. sell orders, order aggressiveness, and order book depth to gauge market sentiment and potential directional biases.
    - **Integration with NLP Sentiment Analysis:**  Combine order book sentiment indicators with sentiment analysis from news feeds or social media to create more comprehensive market sentiment signals for enhanced trading decisions.

## Data Inputs

The Order Book Monitor Agent primarily relies on the following data inputs:

*   **Real-time Binance Order Book Data:**
    - **Data Source:**  Binance Exchange API (WebSocket or REST API endpoints for order book data).
    - **Data Type:** Level 2 or Level 3 order book data for the configured trading pair, providing a snapshot of the current order book depth, bid and ask prices, and order sizes at different price levels.
    - **Data Frequency:** Continuous, real-time updates to capture dynamic order book changes and ensure timely detection of large orders.
    - **Configuration:**  Users need to specify the `TRADING_PAIR` parameter to define which trading pair's order book should be monitored on Binance.
*   **Real-time Price Data from Binance:**
    - **Data Source:** Binance Exchange API (endpoints for fetching current price tickers or real-time price streams).
    - **Data Type:** Real-time price data for the configured `TRADING_PAIR`, used to calculate the USD value of orders for threshold comparison and alerting.
    - **Purpose:**  Essential for converting order sizes in the base currency (e.g., BTC) to USD values for comparison against the `LARGE_ORDER_THRESHOLD_USD` parameter.
*   **Agent Configuration Parameters:**
    - **Configuration Source:** Environment variables (`.env` file) and potentially a configuration file (e.g., `agent_config.yaml`).
    - **Key Parameters:**
      - `TRADING_PAIR`: Specifies the trading pair to monitor (e.g., `"BTC/USDT"`).
      - `LARGE_ORDER_THRESHOLD_USD`: Defines the USD value threshold for large order detection (e.g., `"1000000"` for $1 million USD).
      - `MONITOR_INTERVAL`: Sets the data fetching and analysis interval (e.g., `"5"` seconds).

## Configuration Parameters

*   **agent\_id**: A unique identifier for the agent instance.
*   **agent\_type**: Must be set to `OrderBookMonitorAgent`.

### Example Configuration (YAML)

```yaml
config:
  agent_id: orderbook_monitor_agent_01
  agent_type: OrderBookMonitorAgent
```

## Example Usage

To run the Order Book Monitor Agent:

1.  **Set Environment Variables:** Configure the required environment variables (`TRADING_PAIR`, `LARGE_ORDER_THRESHOLD_USD`, `MONITOR_INTERVAL`) in your `.env` file or directly in your terminal environment.
2.  **Run the Agent Script:** Execute the `orderbook_monitor_agent.py` script from the command line:

    ```bash
    python src/agents/orderbook_monitor_agent.py
    ```

    The agent will start monitoring the order book and output alerts to the console when large orders are detected.

## Output and Monitoring

*   **Real-time Console Alerts:** When a large order (exceeding the configured USD threshold) is detected in the Binance order book, the agent will print an alert message to the console, including:
    *   Timestamp of the alert.
    *   Trading pair being monitored.
    *   Side (BUY or SELL) of the large order.
    *   Size of the large order (in the base currency).
    *   Price of the large order.
    *   USD value of the large order.
*   **Logs:** Basic logging of agent activity and configuration loading.

## Customization Notes

*   **Configure via Environment Variables:**  The primary way to customize the agent is through environment variables, allowing you to easily change the trading pair, large order threshold, and monitoring interval.
*   **Extend Alerting Mechanisms:**  The current agent only provides console alerts. You can extend the `AlertManager` component to add more sophisticated alerting methods beyond console output.
*   **Adjust Order Book Analysis Logic:**  The `OrderBookAnalyzer` component can be customized to implement more complex order book analysis logic beyond simple threshold detection. You could add features to:
    *   Detect order clusters or walls.
    *   Analyze order book depth and imbalances.
    *   Identify spoofing or layering patterns.
*   **Support More Exchanges:**  The current agent is specific to Binance. You can extend the `OrderBookFetcher` and `PriceFetcher` components to support other cryptocurrency exchanges by integrating with their APIs.
*   **Integrate with Trading Strategies:**  The alerts generated by this agent can be used as signals for other trading agents or strategies within the `afz1` framework.

## Code Location

*   `src/agents/orderbook_monitor_agent.py`

## Components

*   **`src/agents/orderbook_monitor_agent.py` (OrderBookMonitorAgent):**  The main agent class that orchestrates order book monitoring, analysis, and alerting.
*   **`src/agents/orderbook_monitor_agent.py` (OrderBookFetcher):**  Fetches order book data from the Binance exchange API.
*   **`src/agents/orderbook_monitor_agent.py` (PriceFetcher):**  Fetches current price data from the Binance exchange API.
*   **`src/agents/orderbook_monitor_agent.py` (OrderBookAnalyzer):**  Analyzes order book data to detect large orders based on the configured threshold.
*   **`src/agents/orderbook_monitor_agent.py` (AlertManager):**  Manages and triggers alerts (currently console alerts).
*   **`src/agents/orderbook_monitor_agent.py` (ConfigurationManager):**  Loads configuration parameters (though currently primarily using environment variables).
*   **`src/agents/base_agent.py` (BaseAgent):** Though `OrderBookMonitorAgent` in the current implementation appears to have a simplified base class within the same file, in a more complete implementation, it would likely inherit from the `BaseAgent` class in `src/agents/base_agent.py` for consistency with other agents.

## Next Steps for Development

*   **Enhance Alerting:**  Extend the `AlertManager` to support more versatile alerting methods beyond console output.
*   **Implement More Sophisticated Order Book Analysis:**  Customize the `OrderBookAnalyzer` to detect more complex order book patterns and signals.
*   **Add Support for More Exchanges:**  Extend the data fetching components to support monitoring order books on additional cryptocurrency exchanges.
*   **Integrate with Trading Strategies:**  Develop example trading strategies that can utilize the alerts generated by the `OrderBookMonitorAgent` to automate trading decisions.
*   **Refactor to Inherit from BaseAgent:**  Refactor `OrderBookMonitorAgent` to properly inherit from `src/agents/base_agent.py` for better consistency and integration with the overall agent framework.