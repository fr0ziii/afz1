# Project Features and Roadmap

This file outlines the current feature stack, development priorities, and roadmap for the afz1 project.

## Feature Roadmap

This roadmap is aligned with the `ROADMAP` section in `docs/README.md` and provides a more detailed view of planned features, categorized by development phase and priority.

### Phase 1: Core Trading Agents (High Priority)

*   **ChartAnalysisAgent Enhancements (High Priority)**
    *   Implement more candlestick patterns (e.g., Three White Soldiers, Dark Cloud Cover).
    *   Add support for more technical indicators (e.g., VWAP, Ichimoku Cloud).
    *   Improve signal generation logic based on combined indicators and patterns.
    *   Implement backtesting capabilities for `ChartAnalysisAgent`.

*   **SniperAgent Development (High Priority)**
    *   Implement core logic for precise entry and exit points.
    *   Integrate with `ChartAnalysisAgent` for signal input.
    *   Implement order execution module for `SniperAgent`.
    *   Backtesting and optimization for `SniperAgent` strategies.

### Phase 2: Information and Alert Agents (Medium Priority)

*   **TweetAgent Enhancements (Medium Priority)**
    *   Improve sentiment analysis accuracy.
    *   Filter tweets based on relevance to specific cryptocurrencies.
    *   Implement alerting based on sentiment shifts.

*   **NewsAgent Development (Medium Priority)**
    *   Develop agent to gather news from crypto news sources.
    *   Implement news summarization and relevance filtering.
    *   Integrate news sentiment analysis.
    *   Alerting on significant news events.

*   **WhaleWatcherAgent Enhancements (Medium Priority)**
    *   Make value threshold configurable.
    *   Support multiple blockchains (e.g., Bitcoin, Solana).
    *   Implement more sophisticated whale behavior analysis.
    *   Alerting for whale transactions.

*   **SentimentAgent Development (Medium Priority)**
    *   Aggregate sentiment data from multiple sources (Twitter, news, social media).
    *   Develop overall market sentiment score.
    *   Integrate sentiment data into trading agents.

*   **RBIAgent Development (Medium Priority)**
    *   Implement Risk-Based Investing principles in agent logic.
    *   Define risk profiles and asset allocation strategies.
    *   Backtesting and optimization for RBI strategies.

*   **OrderBookMonitorAgent Enhancements (Medium Priority)**
    *   Support more exchanges beyond Binance BTC/USDT.
    *   Make order size threshold configurable.
    *   Implement more complex order book analysis (beyond large orders).
    *   Enhanced alerting mechanisms.

### Phase 3: Advanced and Specialized Agents (Low Priority)

*   **FundingAgent Enhancements (ON HOLD - Low Priority)**
    *   Configurable Funding Rate Threshold
    *   Configurable Trading Pairs
    *   Implement Slippage Control
    *   Configurable Spot Order Type
    *   Enhanced Logging
    *   Improved Error Handling

*   **FundingArbAgent Development (Low Priority)**
    *   Implement arbitrage trading strategies based on funding rate discrepancies.
    *   Risk management for arbitrage trades.
    *   Backtesting and optimization.

*   **LiquidationAgent Development (Low Priority)**
    *   Develop agent to capitalize on liquidation events.
    *   Risk assessment and management for liquidation trading.

*   **ListingArbAgent Development (Low Priority)**
    *   Implement arbitrage strategies for new listings.
    *   Real-time monitoring of new listings across exchanges.

*   **NewOrTopAgent Development (Low Priority)**
    *   Identify and trade new or top-performing cryptocurrencies.
    *   Define metrics for "new" and "top-performing".
    *   Risk management for trading volatile new assets.

*   **RiskAgent Development (Low Priority)**
    *   Develop comprehensive risk assessment and management agent.
    *   Integrate risk analysis into other agents.
    *   Implement portfolio risk monitoring.

*   **SolanaAgent Development (Low Priority)**
    *   Specialized agent for Solana ecosystem opportunities (if applicable).
    *   Explore Solana-specific DeFi and trading opportunities.

*   **TXAgent Development (Low Priority)**
    *   Agent for monitoring and analyzing blockchain transactions in detail.
    *   Advanced transaction pattern recognition.

*   **VideoAgent Development (Low Priority)**
    *   Agent for analyzing video content related to market trends.
    *   Natural language processing of video transcripts.
    *   Sentiment analysis from video content.

*   **PhoneAgent Development (Low Priority)**
    *   Agent for real-time alerts and notifications via phone (SMS, voice).
    *   Integration with notification services (e.g., Twilio).

*   **ClipsAgent Development (Low Priority)**
    *   Agent for creating and managing video clips of market analysis.
    *   Automated video generation from agent outputs.

*   **ChatAgent Development (Low Priority)**
    *   Agent for interacting with market participants in chat platforms (e.g., Telegram, Discord).
    *   Automated communication and information dissemination.

*   **CodeRunnerAgent Development (Low Priority)**
    *   Agent for executing and managing custom code and scripts.
    *   Integration with scripting environments.

*   **CopyBotAgent Development (Low Priority)**
    *   Agent to replicate successful trading strategies from other sources.
    *   Strategy mirroring and adaptation.

*   **FocusAgent Development (Low Priority)**
    *   Agent to maintain focus and optimize trading based on specific goals.
    *   Goal-driven trading strategy adjustments.

*   **WhaleAgent Development (Low Priority)**
    *   Agent to simulate and analyze the behavior of large market participants.
    *   Market simulation and scenario analysis.

This roadmap is subject to change based on development progress, community feedback, and market conditions.

<!-- Add more features below as needed -->