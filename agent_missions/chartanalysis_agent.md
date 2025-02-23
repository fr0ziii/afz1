# Chart Analysis Agent Mission

## Description

The Chart Analysis Agent is designed to perform technical analysis on cryptocurrency charts. It utilizes various technical indicators and pattern recognition techniques to identify potential trading signals and insights.

## Functionality

- Fetches chart data from Binance.
- Calculates technical indicators such as SMA, EMA, RSI, and MACD.
- Identifies chart patterns (currently placeholder).
- Generates trading signals (currently placeholder).

## Configuration

The agent is configured via a JSON configuration file, which specifies:

- `agent_id`: Unique identifier for the agent instance.
- `agent_type`:  Agent type (ChartAnalysisAgent).
- `data_source`: Data source (e.g., "binance").
- `exchange`:  Cryptocurrency exchange (e.g., "Binance").
- `trading_pair`: Trading pair (e.g., "XRP/USDT").
- `timeframe`:  Chart timeframe (e.g., "5m").
- `indicators`: List of technical indicators to calculate.
- `indicator_periods`: Periods for each indicator.
- `patterns`: List of chart patterns to recognize.

## Usage

To run the agent, execute the `chartanalysis_agent.py` script.

```bash
python src/agents/chartanalysis_agent.py
```

## File Link

- [Chart Analysis Agent Code](src/agents/chartanalysis_agent.py)
