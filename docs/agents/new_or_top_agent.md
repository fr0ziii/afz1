# New Or Top Agent

## Description

The New Or Top Agent is designed for monitoring new or top trending tokens and listings in cryptocurrency markets. It provides a basic framework for agents that can identify newly listed cryptocurrencies or tokens that are currently trending based on various metrics (e.g., price increase, volume surge, social media buzz). This agent can be valuable for traders looking to capitalize on the initial hype and momentum associated with new listings or trending tokens.

## Missions

[Description of the missions this agent is designed to accomplish. Link to mission files if applicable.]
- Currently, no specific mission files are defined for the New Or Top Agent. Missions would be defined based on the specific monitoring strategies and criteria for identifying new or top trending tokens it is intended to handle.

## Configuration

The New Or Top Agent inherits basic configuration parameters from the `BaseAgent`. Specific configurations for data sources, monitoring criteria, and exchanges would be defined in the agent's configuration.

-   **agent_id**: A unique identifier for the agent instance.
-   **agent_type**: Must be set to `NewOrTopAgent`.

### Example Configuration

```yaml
config:
  agent_id: new_or_top_agent_01
  agent_type: NewOrTopAgent
  # Add any new or top tokens monitoring specific configurations here in the future
  # e.g., exchanges, trending_criteria, new_listing_sources, top_token_metrics
```

## Inputs and Outputs

### Inputs

-   **Market Data**: Real-time market data from cryptocurrency exchanges to identify trending tokens (e.g., price, volume).
-   **Listing Data**: Information about new cryptocurrency listings from various sources.
-   **Social Media Data**: (Optional) Social media trends and sentiment data to gauge token popularity.

### Outputs

-   **New Token Alerts**: Alerts for newly listed cryptocurrencies that meet certain criteria.
-   **Top Trending Token Alerts**: Alerts for top trending tokens based on defined metrics.
-   **Token Analysis**:  Analysis of new or top tokens, potentially including performance metrics, social sentiment analysis, and visualizations (future implementation).
-   **Logs**: Informational and error logs for monitoring agent activity and debugging.

## Workflow

1.  **Monitor New Listings**: The agent monitors various sources for announcements of new cryptocurrency listings (currently placeholder logic).
2.  **Identify Top Trending Tokens**: The agent analyzes market data to identify top trending tokens based on predefined metrics (e.g., price increase, volume surge) (currently placeholder logic).
3.  **Generate Alerts**: The agent generates alerts for newly listed or top trending tokens that meet specific criteria (currently placeholder logic).
4.  **Output Analysis**:  In future implementations, the agent can output more detailed analysis of new or top tokens.
5.  **Log Activity**: The agent logs monitoring activities, analysis results, and generated alerts for monitoring and analysis.

## Example Usage

To run the New Or Top Agent, you would instantiate and run the agent, configuring it with data sources, monitoring criteria, and exchanges. Since the current implementation is basic, the example usage primarily involves setting up the agent and potentially adding monitoring logic.

```python
from src.agents.new_or_top_agent import NewOrTopAgent

config = {
  "agent_id": "new_or_top_agent_01",
  "agent_type": "NewOrTopAgent",
}

agent = NewOrTopAgent(config)
# agent.run() # Run method currently placeholder
# Example of configuring exchanges and trending criteria (to be implemented)
# config["exchanges"] = ["Binance", "Coinbase"]
# config["trending_criteria"] = {"price_increase_percent": 10, "volume_surge_percent": 200}
# agent = NewOrTopAgent(config)
# agent.start_monitoring_new_or_top_tokens() # Method to initiate monitoring (to be implemented)
```

This example shows the basic instantiation of the New Or Top Agent. The `run` method is currently a placeholder and would need to be implemented with actual monitoring logic. Future implementations would include methods to configure exchanges, monitoring criteria, and initiate monitoring.

## Code Location

-   `src/agents/new_or_top_agent.py`

## Components

-   **`src/agents/base_agent.py` (BaseAgent)**: The New Or Top Agent inherits basic agent functionalities from the `BaseAgent`.
-   **Data Monitoring Components (To be implemented)**: Future implementations would include components for monitoring market data, listing sources, and potentially social media data.
-   **Analysis Components (Future)**: Components for analyzing market data and identifying new or top trending tokens based on defined criteria.
-   **Alerting Components (Future)**: Components for generating and delivering alerts for new or top tokens.

## Notes and Considerations

-   **Placeholder Implementation**: The current `NewOrTopAgent` is a basic placeholder. Significant implementation is required to add actual monitoring and analysis capabilities.
-   **Data Source Integration**:  Implementing data source integration would involve handling APIs for market data, listing information, and potentially social media data.
-   **Trending Criteria Definition**:  Define clear and effective criteria for identifying top trending tokens based on relevant metrics.
-   **New Listing Detection**:  Implement robust mechanisms for detecting new cryptocurrency listings from various sources.
-   **Timeliness of Data**:  Ensure timely access to market data and listing information, as the relevance of new or top token opportunities can be short-lived.