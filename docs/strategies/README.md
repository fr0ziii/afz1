# Strategy Guide

This guide explains how to create, implement, and backtest trading strategies within the `afz1` framework.

## Strategy Framework Overview

The `afz1` project provides a flexible framework for developing and deploying custom trading strategies. Strategies are implemented as Python classes within the `src/strategies/` directory, inheriting from the `base_strategy.py` class.

*   **`base_strategy.py`**: Defines the abstract `BaseStrategy` class, which serves as the foundation for all trading strategies. It outlines the required methods that each strategy must implement.
*   **`example_strategy.py`**: Provides a basic example strategy implementation to demonstrate the framework and serve as a starting point for creating custom strategies.
*   **`custom/` Directory**:  The `src/strategies/custom/` directory is designated for users to create and store their own custom trading strategies.

## Creating a Custom Strategy

Follow these steps to create your own trading strategy:

1.  **Create a New Python File:**
    In the `src/strategies/custom/` directory, create a new Python file (e.g., `my_strategy.py`).

2.  **Import `BaseStrategy`:**
    In your new file, import the `BaseStrategy` class:

    ```python
    from src.strategies.base_strategy import BaseStrategy
    ```

3.  **Define Your Strategy Class:**
    Create a class that inherits from `BaseStrategy` and implement the required methods:

    ```python
    class MyTradingStrategy(BaseStrategy):
        def __init__(self, config):
            super().__init__(config)
            # Initialize strategy-specific parameters here

        def initialize(self):
            """Initialization logic for the strategy (e.g., data loading, indicator setup)."""
            pass

        def process_data(self, market_data):
            """Process incoming market data."""
            pass

        def generate_signal(self):
            """Generate trading signals based on processed data."""
            return None  # Return a trading signal or None

        def execute_trade(self, signal):
            """Execute trades based on generated signals."""
            if signal:
                # Implement order placement logic here
                pass
    ```

4.  **Implement Strategy Logic:**
    Fill in the logic for each method in your strategy class:

    *   **`__init__(self, config)`**:  Initialize any strategy-specific parameters from the `config` dictionary.
    *   **`initialize(self)`**:  Perform any setup tasks needed at the start of trading or backtesting (e.g., loading historical data, initializing technical indicators).
    *   **`process_data(self, market_data)`**:  Process incoming market data (OHLCV, order book, etc.) and update strategy state.
    *   **`generate_signal(self)`**:  Implement your core trading logic to generate buy/sell signals based on processed data and strategy rules.
    *   **`execute_trade(self, signal)`**:  Implement the logic to execute trades based on the generated signal. This might involve calling a trading agent or order execution module.

5.  **Configuration Options:**
    Define any configurable parameters for your strategy in the `__init__` method and document them. Users can then adjust these parameters in configuration files or through the web interface (if implemented).

## Backtesting Strategies

The `afz1` project includes a backtesting framework in `src/data/rbi/backtests/` to evaluate the performance of your strategies.

1.  **Navigate to Backtesting Directory:**
    ```bash
    cd src/data/rbi/backtests/
    ```

2.  **Run Backtesting Scripts:**
    Execute the provided backtesting scripts (e.g., `python BollingerBands_BT.py`). You may need to modify these scripts to use your custom strategy class and configure backtesting parameters.

3.  **Interpreting Backtesting Results:**
    Backtesting scripts typically output performance metrics and generate charts in the `charts/` and `stats/` subdirectories. Analyze these results to evaluate your strategy's historical performance. Key metrics to consider include:

    *   **Sharpe Ratio:**  Risk-adjusted return.
    *   **Drawdown:**  Maximum loss from peak to trough.
    *   **Total Profit/Loss:**  Net profit or loss over the backtesting period.
    *   **Win Rate:**  Percentage of winning trades.

4.  **Customizing Backtesting:**
    You can modify existing backtesting scripts or create new ones to:

    *   Backtest different strategies.
    *   Adjust backtesting parameters (date ranges, trading pairs, initial capital).
    *   Incorporate different data sources.
    *   Calculate additional performance metrics.

## Integrating Strategies with Agents

To use your custom strategy with a trading agent for live or paper trading, you will need to:

1.  **Configure the Trading Agent:**  Modify the configuration of the `trading_agent.py` or `strategy_agent.py` to use your custom strategy class. This typically involves specifying the strategy class name and any required strategy parameters in the agent's configuration.
2.  **Run the Agent:**  Start the trading agent. The agent will then use your implemented strategy to generate trading signals and execute trades (depending on the agent's design).

## Example Strategies Walkthrough

(Provide a detailed walkthrough of `example_strategy.py` and potentially other example strategies, explaining the code logic, indicators used, signal generation rules, and configuration options.)

By following this guide, you can effectively create, backtest, and deploy your own custom trading strategies within the `afz1` project.
