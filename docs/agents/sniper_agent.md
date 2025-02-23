# Sniper Agent (`sniper_agent.py`)

## Purpose

The Sniper Agent is designed to execute precise, short-term "sniper" trading strategies in cryptocurrency markets. This agent focuses on identifying high-probability entry and exit points for trades, aiming to capitalize on short-lived market movements with precision. While the current implementation provides a basic framework, future versions will incorporate more sophisticated sniper trading strategies.

## Functionality

*   **Basic Sniper Trading Framework:** Provides a foundational structure for implementing sniper trading strategies.
*   **Entry Point Detection (To be implemented):** Future implementations will incorporate various techniques for identifying precise entry points for trades, such as:
    *   **Technical Indicator-Based Signals:**  Using technical indicators (e.g., RSI, MACD, Stochastic Oscillator) to identify overbought or oversold conditions or momentum shifts.
    *   **Chart Pattern Recognition:**  Identifying specific candlestick patterns or chart formations that suggest high-probability entry points.
    *   **Order Book Analysis:**  Analyzing order book data to detect support and resistance levels or order imbalances that may indicate entry points.
*   **Exit Point Determination (To be implemented):** Future versions will implement logic for determining precise exit points for trades, including:
    *   **Profit Target Setting:**  Setting predefined profit targets based on technical analysis or risk-reward ratios.
    *   **Stop-Loss Order Placement:**  Implementing stop-loss orders to limit potential losses if trades move against expectations.
    *   **Trailing Stop-Loss Logic:**  Potentially using trailing stop-loss orders to lock in profits as prices move favorably.
*   **Order Execution (To be implemented):**  Future features will include automated order execution capabilities for sniper trades, involving:
    *   **Exchange API Integration:**  Connecting to exchange APIs to place orders with precision.
    *   **Limit Order Placement:**  Primarily using limit orders to enter and exit trades at desired price levels.
    *   **Order Size Calculation:**  Determining appropriate order sizes based on risk management parameters and entry point confidence.
*   **Risk Management for Sniper Trading (To be implemented):**  Future versions will incorporate risk management features specific to sniper trading, such as:
    *   **Strict Stop-Loss Enforcement:**  Emphasizing the importance of and strictly enforcing stop-loss orders to limit losses in fast-moving markets.
    *   **Position Size Limits:**  Using smaller position sizes for sniper trades due to their short-term nature and potential for rapid price reversals.
    *   **Slippage Control:**  Managing slippage when executing orders, especially in volatile market conditions.
*   **Performance Monitoring (To be implemented):**  Future versions will provide tools for monitoring the performance of sniper trading strategies, tracking metrics like:
    *   **Win Rate:**  Percentage of profitable trades.
    *   **Profit Factor:**  Ratio of gross profit to gross loss.
    *   **Average Profit per Trade:**  Average profit per winning trade.
    *   **Average Loss per Trade:**  Average loss per losing trade.
    *   **Risk-Adjusted Return Metrics:**  Sharpe Ratio, Sortino Ratio, etc.

## AI Model(s) Used

*   None directly in the current basic implementation.
*   AI models could potentially be used in future versions for:
    *   **Entry/Exit Point Prediction:**  Using machine learning to predict high-probability entry and exit points for sniper trades.
    *   **Dynamic Parameter Optimization:**  Optimizing sniper trading strategy parameters (indicator thresholds, pattern recognition settings, stop-loss levels) using machine learning.
    *   **Risk Assessment:**  AI-powered risk assessment for sniper trades, considering factors like market volatility and order book dynamics.

## Data Inputs

*   **Market Data:** Real-time market data, including candlestick data, order book data, and potentially social sentiment data.
*   **Trading Strategy Parameters (To be configured in subclasses):**  Parameters defining the specific sniper trading strategy being used (indicator settings, pattern definitions, risk-reward ratios).

## Configuration Parameters

*   **agent\_id**: A unique identifier for the agent instance.
*   **agent\_type**: Must be set to `SniperAgent`.
*   **Strategy-Specific Configuration (To be defined in subclasses):** Concrete subclasses will define their own configuration parameters for their specific sniper trading strategies.

### Example Configuration (YAML - Base Class)

```yaml
config:
  agent_id: sniper_agent_base_01
  agent_type: SniperAgent
```

**Note:** This configuration is for the abstract base class. Concrete subclasses of `SniperAgent` will require their own specific configurations for their sniper trading strategies.

## Example Usage

To use the `SniperAgent`, you would typically create a subclass that implements a specific sniper trading strategy and then instantiate and run the subclassed agent. The base `SniperAgent` class itself is abstract and not meant to be run directly.

```python
# Example of how a concrete subclass might be implemented (conceptual)
from src.agents.sniper_agent import SniperAgent

class RSISniperAgent(SniperAgent): # Example subclass using RSI for entry signals
    def __init__(self, config):
        super().__init__(config)
        # Load RSI-specific configuration
        self.rsi_oversold_threshold = config.get("rsi_oversold_threshold", 30) # Example config
        self.profit_target_percent = config.get("profit_target_percent", 0.01) # Example config
        self.stop_loss_percent = config.get("stop_loss_percent", 0.005) # Example config

    def run(self):
        # Implement RSI-based entry signal detection, order execution, and risk management logic here
        current_rsi = self.calculate_rsi() # Example method to get RSI value
        if current_rsi < self.rsi_oversold_threshold:
            entry_price = self.determine_entry_price() # Example method
            # Place limit buy order
            self.place_limit_buy_order(entry_price, stop_loss_percent=self.stop_loss_percent, profit_target_percent=self.profit_target_percent)
            self._log_info(f"RSI entry signal detected. Placed limit buy order at {entry_price}")
        else:
            self._log_debug("No RSI entry signal detected")

        self._log_info("Sniper trading cycle completed")


# Example configuration for the concrete subclass
config = {
    "agent_id": "rsi_sniper_agent_01",
    "agent_type": "RSISniperAgent", # Assuming RSISniperAgent is the subclass name
    "rsi_oversold_threshold": 25, # Example RSI threshold
    "profit_target_percent": 0.015, # Example profit target
    "stop_loss_percent": 0.0075 # Example stop loss
}

agent = RSISniperAgent(config)
agent.run()
```

**Note:** The `RSISniperAgent` example above is conceptual and would require further implementation of RSI calculation, order placement, and more complete trading logic.

## Output and Monitoring

*   **Executed Sniper Trades (Output by subclasses):** Concrete subclasses will output details of executed sniper trades, including entry and exit prices, order sizes, and profit/loss.
*   **Performance Metrics (Output by subclasses):** Subclasses will track and output performance metrics for their sniper trading strategies (win rate, profit factor, risk-adjusted returns).
*   **Trading Signals (Internal logging):**  Internal logging of detected entry and exit signals and trading decisions.
*   **Logs:**  Logs basic agent activity and configuration loading from the base class. Subclasses should extend logging for their specific functionalities and trading logic.

## Customization Notes

*   **Create Concrete Sniper Strategy Subclasses:**  To implement specific sniper trading strategies, you need to create concrete subclasses of `SniperAgent` for each strategy (e.g., `RSISniperAgent`, `PatternSniperAgent`, `OrderBookSniperAgent`).
*   **Implement Entry/Exit Point Detection Logic:**  Within subclasses, implement methods to detect precise entry and exit points based on technical indicators, chart patterns, order book analysis, or other techniques.
*   **Define Risk Management Rules:**  Configure and implement strict risk management rules within subclasses, including stop-loss orders and position sizing limits.
*   **Backtest and Optimize Strategies:**  Thoroughly backtest and optimize sniper trading strategies implemented in subclasses to evaluate their effectiveness and identify optimal parameters.
*   **AI-Powered Sniper Strategies in Subclasses:**  Incorporate AI models within subclasses to enhance entry/exit point prediction, dynamically optimize strategy parameters, or adapt to changing market conditions.

## Code Location

*   `src/agents/sniper_agent.py`

## Components

*   **BaseAgent (`src/agents/base_agent.py`):**  The `SniperAgent` class inherits from `BaseAgent`, providing the basic agent lifecycle methods and configuration loading.

## Next Steps for Development

*   **Develop Concrete Sniper Agent Subclasses:** Create example subclasses of `SniperAgent` that implement specific sniper trading strategies (e.g., `RSISniperAgent`, `PatternSniperAgent`).
*   **Implement Entry/Exit Signal Detection:** Within subclasses, implement methods to detect entry and exit signals based on chosen technical analysis techniques.
*   **Add Order Execution Logic:** Implement basic order execution logic within subclasses to place limit orders for sniper trades.
*   **Incorporate Risk Management Rules:**  Add stop-loss and position sizing risk management rules to subclasses.
*   **Backtesting Framework Integration:**  Integrate a backtesting framework to evaluate and optimize sniper trading strategies.