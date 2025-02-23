# New Or Top Agent (`new_or_top_agent.py`)

## Purpose

The New Or Top Agent is designed to proactively monitor two distinct yet potentially lucrative segments of the cryptocurrency market: new cryptocurrency listings and top-performing tokens. By focusing on these areas, the agent aims to:

*   **Capitalize on New Listing Price Surges:**  Newly listed cryptocurrencies often experience significant initial price surges due to hype, speculation, and early adoption. The agent aims to detect these listings early and identify potential short-term trading opportunities during the initial price discovery phase.
*   **Identify Momentum-Driven Top Performers:**  Top-performing cryptocurrencies exhibiting strong upward momentum can present swing trading or trend-following opportunities. The agent monitors market data to identify tokens with significant price gains and sustained momentum, signaling potential long opportunities.
*   **Provide Early Signals for High-Growth Potential:**  New listings and top performers can sometimes represent early signals of high-growth potential cryptocurrencies. By tracking these segments, the agent can help users discover promising new projects or tokens with strong market traction.
*   **Generate Actionable Trading Opportunities:**  By combining new listing and top performer data, the agent aims to generate actionable trading opportunities for users seeking to capitalize on both short-term listing surges and longer-term momentum trends.
*   **Offer Diversified Opportunity Identification:**  Provides a diversified approach to opportunity identification by monitoring both newly emerging assets (new listings) and established assets with strong market momentum (top performers), capturing a broader spectrum of potential trading scenarios.

The New Or Top Agent serves as a valuable tool for traders and investors seeking to identify and capitalize on the unique opportunities presented by both the novelty of new listings and the momentum of top-performing cryptocurrencies.

## Functionality

The New Or Top Agent is designed to provide a comprehensive set of functionalities for monitoring and analyzing new and top-performing cryptocurrencies:

*   **Real-time New Listing Monitoring and Data Aggregation:**
    - **Continuous Monitoring of Listing Sources:**  Continuously monitor various sources for new cryptocurrency listing announcements, including cryptocurrency exchanges, listing aggregators, and news channels.
    - **Rapid Listing Data Acquisition:**  Implement efficient data acquisition mechanisms to capture new listing information promptly as it becomes available.
*   **Top Performer Identification and Ranking:**
    - **Market Data Monitoring:**  Continuously monitor market data from cryptocurrency exchanges to identify top-performing tokens based on various metrics.
    - **Configurable Performance Metrics:**  Allow users to configure performance metrics for identifying top performers, such as:
      - **Price Change Percentage:**  Identify tokens with the highest percentage price increase over different timeframes (e.g., 1 hour, 24 hours, 7 days).
      - **Trading Volume Increase:**  Track tokens with significant surges in trading volume as indicators of growing interest and momentum.
      - **Social Sentiment Analysis:** (Future) Integrate sentiment analysis data to identify tokens with positive or rapidly improving social media sentiment.
    - **Performance Ranking and Filtering:**  Rank top-performing tokens based on selected metrics and allow users to filter results based on criteria such as market capitalization, trading volume, or exchange listings.
*   **Automated Opportunity Scoring and Prioritization:**
    - **Opportunity Scoring Algorithm:**  Develop an algorithm to automatically score and prioritize potential trading opportunities based on a combination of new listing signals and top performer metrics.
    - **Customizable Scoring Weights:**  Allow users to customize the weighting of different factors (e.g., new listing status, price change percentage, volume increase, sentiment score) in the opportunity scoring algorithm to align with their trading preferences.
*   **Alerting and Reporting Mechanisms:**
    - **Real-time New Listing Alerts:**  Generate instant alerts when new cryptocurrency listings are detected on monitored exchanges, providing timely notification of potential early entry opportunities.
    - **Periodic Top Performer Reports:**  Generate periodic reports (e.g., daily, weekly) listing top-performing tokens based on user-defined metrics and ranking criteria.
    - **Opportunity Summary Dashboards:** (Future) Develop interactive dashboards to visualize and summarize identified trading opportunities, new listings, and top performer data, providing users with a consolidated overview of potential trades.
*   **Risk Management and Volatility Considerations:**
    - **Volatility Indicators:**  Integrate volatility indicators (e.g., Average True Range - ATR, Volatility Percentile) to assess the volatility of new and top-performing tokens, enabling users to adjust risk parameters accordingly.
    - **Position Sizing Recommendations:** (Future) Provide AI-driven position sizing recommendations for trading new and top-performing tokens, considering their volatility and risk profiles to manage capital allocation and limit potential losses.
    - **Stop-Loss and Take-Profit Suggestions:** (Future) Incorporate AI-powered models to suggest dynamic stop-loss and take-profit levels for trades on new and top-performing tokens, optimizing risk-reward ratios and trade management.

## AI Model(s) Used

*   None directly in the current basic implementation.
*   AI models could potentially be used in future versions for:
    *   **Listing Prediction:**  Predicting cryptocurrencies that are likely to become top performers or be newly listed on major exchanges.
    *   **Volatility Analysis:**  Analyzing the volatility patterns of new and top-performing tokens to optimize trading strategies and risk management.
    *   **Sentiment Analysis:**  Monitoring social media and news sentiment to gauge the sustainability of top performer momentum.

## Data Inputs

*   **New Listing Data:** Data sources for new cryptocurrency listings (APIs, aggregators).
*   **Market Data:** Real-time market data to identify top-performing tokens (price, volume, etc.).
*   **(Optional) Social Media Data:** Social media data for sentiment analysis of trending tokens.

## Configuration Parameters

*   **agent\_id**: A unique identifier for the agent instance.
*   **agent\_type**: Must be set to `NewOrTopAgent`.

### Example Configuration (YAML)

```yaml
config:
  agent_id: new_or_top_agent_01
  agent_type: NewOrTopAgent
```

## Example Usage

To instantiate and run the `NewOrTopAgent`:

```python
from src.agents.new_or_top_agent import NewOrTopAgent

config = {
    "agent_id": "new_or_top_agent_01",
    "agent_type": "NewOrTopAgent",
}

agent = NewOrTopAgent(config)
agent.run()
```

**Note:** The current implementation of `NewOrTopAgent` provides a basic framework. To add actual new and top token monitoring and trading capabilities, you would need to extend the `NewOrTopAgent` class and implement the following:

1.  **New Listing Data Integration:** Implement connections to sources of new listing data.
2.  **Top Performer Data Integration:** Integrate with market data APIs to gather data for identifying top-performing tokens.
3.  **Opportunity Detection Logic:** Develop logic to identify trading opportunities based on new listings and top performer metrics.
4.  **Alerting and Reporting Mechanisms:** Implement features for real-time alerts and periodic reports on new listings and top performers.
5.  **Risk Management Features:** Incorporate risk management features specific to trading highly volatile new and top-performing tokens.
6.  **Trading Strategy Integration (Optional):**  Integrate with trading strategy modules to automate trading based on identified opportunities.

## Output and Monitoring

*   **New Listing Alerts:**  Real-time alerts for new cryptocurrency listings.
*   **Top Performer Reports:**  Periodic reports listing top-performing tokens and their metrics.
*   **Opportunity Summary Reports:**  Reports summarizing potential trading opportunities identified by the agent.
*   **Logs:**  Logs basic agent activity and any errors encountered.

## Customization Notes

*   **Extend for More Data Sources:**  Customize the agent to monitor a wider range of new listing sources and market data providers.
*   **Implement Different Top Performer Metrics:**  Allow users to configure different metrics for identifying top-performing tokens (e.g., different timeframes, volume thresholds, sentiment scores).
*   **Develop Specific Trading Strategies:**  Design and integrate trading strategies tailored to capitalize on new listing surges and top performer momentum.
*   **AI-Powered Opportunity Scoring:**  Incorporate AI models to score and rank potential trading opportunities based on new listing and top performer data, considering factors like volatility, liquidity, and market sentiment.

## Code Location

*   `src/agents/new_or_top_agent.py`

## Components

*   **BaseAgent (`src/agents/base_agent.py`):**  The `NewOrTopAgent` class inherits from `BaseAgent`, providing the basic agent lifecycle methods and configuration loading.

## Next Steps for Development

*   **Implement New Listing Data Integration:** Choose sources for new listing data and implement data ingestion.
*   **Develop Top Performer Identification Logic:** Implement algorithms to identify top-performing tokens based on market data.
*   **Add Alerting and Reporting Features:** Implement basic alerting and reporting mechanisms for new listings and top performers.
*   **Incorporate Risk Management for Volatile Tokens:**  Add risk management controls specific to trading new and top-performing tokens.
*   **User Interface for Configuration:**  Develop a user interface to allow users to configure monitoring parameters and alerting preferences.