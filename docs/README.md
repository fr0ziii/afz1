# afz1 Project Documentation

Welcome to the documentation for the `afz1` project, an open-source framework for AI-powered cryptocurrency trading agents. This documentation is designed to guide you through setting up, understanding, using, and contributing to the `afz1` project.

## Documentation Sections

*   **[Setup and Installation Guide](./setup/README.md)**: Learn how to install and configure the `afz1` project environment.
*   **[Agent Guide](./agents/README.md)**: Explore the functionalities and configurations of the various AI trading agents.
*   **[Chart Analysis Agent Documentation](./agents/chartanalysis_agent.md)**: In-depth documentation for the Chart Analysis Agent.
*   **[Strategy Guide](./strategies/README.md)**: Discover how to create, implement, and backtest trading strategies within the framework.
*   **[Data Guide](./data/README.md)**:  Understand the data sources, API, and data management within `afz1`.
*   **[Model Guide](./models/README.md)**:  Learn about AI model integrations and the model factory.
*   **[Web Interface Guide](./web/README.md)**:  Get instructions on using the web-based user interface.
*   **[Contribution Guide](./contributing/README.md)**:  Find guidelines for contributing to the `afz1` project.
*   **[Troubleshooting Guide](./troubleshooting/README.md)**:  Solutions to common issues and errors.
*   **[Glossary of Terms](./glossary/README.md)**:  Definitions of key terms used in the project.

## ROADMAP

- **Phase 1: Core Trading Agents**
    - `ChartAnalysisAgent`: Agent for analyzing market charts and identifying patterns.
    - `SniperAgent`: Agent focused on precise entry and exit points for trades.

- **Phase 2: Information and Alert Agents**
    - `TweetAgent`: Agent for monitoring and analyzing Twitter for market sentiment.
    - `NewsAgent`: (To be created) Agent for gathering and interpreting news relevant to crypto markets.
    - `WhaleWatcherAgent`: Agent to track large transactions and potential market movers.
    - `SentimentAgent`: Agent to analyze overall market sentiment from various sources.
    - `RBIAgent`: (To be created) Agent based on Risk-Based Investing principles.
    - `OrderBookMonitorAgent`: Agent to monitor Binance BTC/USDT order book for large orders (over 1M USDT) and trigger alerts.

- **Phase 3: Advanced and Specialized Agents**
    - `FundingAgent`: Agent for managing funding rates and optimizing funding strategies.
    - `FundingArbAgent`: Agent for arbitrage trading based on funding rate discrepancies.
    - `LiquidationAgent`: Agent to capitalize on liquidation events in the market.
    - `ListingArbAgent`: Agent for arbitrage trading on new listings.
    - `NewOrTopAgent`: Agent to identify and trade new or top-performing cryptocurrencies.
    - `RiskAgent`: Agent for comprehensive risk assessment and management.
    - `SolanaAgent`: (If applicable) Specialized agent for Solana ecosystem opportunities.
    - `TXAgent`: Agent for monitoring and analyzing blockchain transactions.
    - `VideoAgent`: Agent for analyzing video content related to market trends.
    - `PhoneAgent`: (To be created) Agent for real-time alerts and notifications via phone.
    - `ClipsAgent`: Agent for creating and managing video clips of market analysis.
    - `ChatAgent`: Agent for interacting with market participants in chat platforms.
    - `CodeRunnerAgent`: Agent for executing and managing custom code and scripts.
    - `CopyBotAgent`: Agent to replicate successful trading strategies from other sources.
    - `FocusAgent`: Agent to maintain focus and optimize trading based on specific goals.
    - `WhaleAgent`: Agent to simulate and analyze the behavior of large market participants.
