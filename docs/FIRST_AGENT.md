**MVP Name:** "afz1 Whale Watcher MVP"

**Core Value Proposition:**  Demonstrates an agent capable of monitoring a cryptocurrency blockchain for large transactions (whales) and logging these events.

**Key Features for MVP:**

1.  **Whale Hunter Agent: `WhaleWatcherAgent`**

      * **Functionality:**
          * **Blockchain Monitoring:** Connects to a blockchain explorer API for a specific cryptocurrency (e.g., Bitcoin, Ethereum). For MVP, focus on **Ethereum** as it's widely used and has readily available explorer APIs.  We can use a free tier API to keep MVP simple.
          * **Transaction Stream:**  Utilizes the blockchain explorer API to access a stream of new transactions on the Ethereum blockchain.
          * **Value Calculation:**
              * For each transaction, retrieves the transaction value in the native cryptocurrency (ETH).
              * Fetches the current ETH-USD price from a price API (e.g., CoinGecko free API is suitable for MVP).
              * Calculates the USD value of the transaction.
          * **Threshold Filtering:** Filters transactions based on the USD value, identifying transactions exceeding $1,000,000 USD.
          * **Whale Transaction Logging:**  Logs details of identified whale transactions to a console and/or a simple log file.  Logged information should include:
              * Transaction Hash
              * Timestamp
              * Value in ETH
              * Value in USD
              * From Address
              * To Address
      * **Configuration:**
          * Cryptocurrency selection (initially just Ethereum).
          * Value threshold (pre-set to $1,000,000 USD for MVP, but could be made configurable later).
          * Blockchain explorer API key (if required by the chosen API, configured via `.env`).
          * Price API key (if required, configured via `.env`).

2.  **Simplified Data Handling**

      * Direct API calls within the `WhaleWatcherAgent` to blockchain explorer and price API.  No need for a complex `MarketDataAPI` for this MVP.
      * Basic JSON parsing of API responses.

3.  **Minimal Output and Monitoring**

      * Console logging of identified whale transactions in a readable format.
      * Optional: Simple text file logging of whale transactions for later review.

4.  **Documentation (MVP Level)**

      * Basic `README.md` outlining:
          * MVP features and limitations of the `WhaleWatcherAgent`.
          * Setup and installation instructions (simplified).
          * Instructions on how to run the `WhaleWatcherAgent`.
          * Explanation of how the agent works (data sources, logic).
          * Disclaimer that this is an MVP for demonstration purposes.

**Technology Choices for MVP:**

  * **Blockchain Explorer API:**  **Etherscan API** ([etherscan.io](https://www.google.com/url?sa=E&source=gmail&q=https://etherscan.io)) is a good choice for Ethereum. They have a free tier suitable for MVP development.  We can use their API to get recent transactions.
  * **Price API:** **Binance API** is used for fetching ETH-USD price.
  * **Programming Language:** Python (as per project context).

**Simplified Implementation Steps:**

1.  **Set up Python Environment:** Follow the simplified setup from the "afz1 Agent Core" MVP or the full setup guide if preferred.
2.  **Install Required Libraries:**  Likely `requests` for making API calls.
3.  **Implement `WhaleWatcherAgent` in `src/agents/whale_watcher_agent.py`:**
      * Include logic to:
          * Connect to Etherscan API to get recent Ethereum transactions.
          * Connect to CoinGecko API to get ETH-USD price.
          * Process transactions, calculate USD value, and filter for whale transactions.
          * Log whale transaction details.
4.  **Create `main.py` in `src/` to run the `WhaleWatcherAgent`.**
5.  **Create a basic `README.md` in the project root.**
6.  **Configure `.env_example` and `.env` for API keys (if needed).**

**Why this "Whale Watcher Agent" MVP is a good starting point:**

  * **Clear and Engaging Concept:** "Whale watching" is a recognizable and interesting concept in crypto, making the MVP easily understandable and potentially engaging for product managers and users.
  * **Demonstrates Real-Time Data Processing:**  Shows the agent's ability to work with real-time blockchain data and external APIs.
  * **Scalable Concept:** The "whale watching" concept can be expanded upon in future iterations to include more sophisticated analysis of whale behavior, alerting mechanisms, and integration with trading strategies.
  * **Relatively Self-Contained:**  The MVP can be implemented as a single agent without requiring complex interactions with other agents or UI components, simplifying development.
