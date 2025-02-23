# afz1 - Autonomous Finance Agents

afz1 is an open-source project dedicated to the development of autonomous agents for decentralized finance (DeFi). These agents are designed to automate and optimize various tasks within the DeFi ecosystem, including trading, portfolio management, risk assessment, market analysis, and information aggregation. The project aims to provide a modular and extensible framework for building sophisticated DeFi agents.

## Project Structure

The project is organized into the following directories:

-   `src/`: Contains the core source code, including agent implementations and reusable components.
-   `src/agents/`: Houses the implementations of various autonomous agents, each designed for a specific DeFi task.
-   `src/components/`: Includes reusable components and modules used by the agents, such as data providers, signal generators, and utility functions.
-   `data/`: Stores data files, datasets, and resources used by the agents.
-   `memory-bank/`: Contains files for maintaining project context, history, and architectural decisions.
-   `agent_missions/`: Defines specific missions and configurations for agents.
-   `docs/`: Project documentation, including agent details, setup guides, and research papers.
-   `.env_example`: Example environment configuration file for API keys and settings.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `README.md`: The current file, providing a project overview and setup instructions.
-   `requirements.txt`: Lists the project's Python dependencies.

## Components

The `src/components/` directory contains reusable modules that provide functionalities to the agents:

-   `binance_data_provider.py`: Fetches real-time and historical market data from the Binance exchange.
-   `chart_data_provider.py`: Provides functionalities for accessing and processing chart data from various sources.
-   `pattern_recognizer.py`: Implements algorithms for recognizing and identifying chart patterns.
-   `signal_generator.py`: Generates trading signals based on market data and analysis.
-   `technical_indicator_calculator.py`: Calculates various technical indicators (e.g., RSI, MACD, moving averages).

## Agents

The `src/agents/` directory contains a diverse set of autonomous agents, each specialized for a specific DeFi task:

-   `base_agent.py`: Abstract base class providing common functionalities for all agents.
-   `chartanalysis_agent.py`: Analyzes cryptocurrency charts to identify trading opportunities.
-   `funding_agent.py`: Manages and optimizes funding strategies in DeFi.
-   `fundingarb_agent.py`: Exploits arbitrage opportunities in funding rate markets.
-   `liquidation_agent.py`: Monitors and reacts to liquidation events in DeFi protocols.
-   `listingarb_agent.py`: Detects and acts on arbitrage opportunities arising from new token listings.
-   `rbi_agent.py`: Focuses on regulatory and compliance aspects in DeFi.
-   `risk_agent.py`: Assesses and manages risks associated with DeFi strategies.
-   `sentiment_agent.py`: Analyzes market sentiment from social media and news sources.
-   `trading_agent.py`: Core agent for executing and managing trading strategies.
-   `tweet_agent.py`: Interacts with Twitter for market updates and sentiment analysis.
-   `whale_agent.py`: Tracks and analyzes large transactions ("whales") for market insights.
-   `whale_watcher_agent.py`: Continuously monitors whale activity for potential market movements.
-   `orderbook_monitor_agent.py`: Monitors order book dynamics for trading signals.

## Agents missions

The `agent_missions/` directory will contain files defining specific agent missions.

-   [Chart Analysis Agent](agent_missions/chartanalysis_agent.md): Agent for analyzing charts.

## Setup and Installation

Follow these steps to set up and install the project:

1.  **Prerequisites:**
    -   Python 3.10 or higher is required.
    -   `pip` package installer.
    -   `venv` for virtual environment management (recommended).
    -   Git for cloning the repository.

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/fr0ziii/afz1
    cd afz1
    ```

3.  **Environment Setup:**

    It is highly recommended to use a virtual environment to isolate project dependencies.

    *   **Using venv (Example):**

        ```bash
        python3.10 -m venv venv
        source venv/bin/activate   # On Linux/macOS
        venv\Scripts\activate  # On Windows
        ```

4.  **Dependency Installation:**

    Install the required Python packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **API Keys Configuration:**

    API keys are required to interact with various services (e.g., Binance, Etherscan).

    *   Copy the `.env_example` file to `.env`:

        ```bash
        cp .env_example .env  # On Linux/macOS
        copy .env_example .env  # On Windows
        ```
    *   Open the `.env` file and add your API keys. Example:

        ```
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        BINANCE_API_KEY=YOUR_BINANCE_API_KEY
        # Add other API keys as needed
        ```

    **Security Note:**  **Never commit the `.env` file with your actual API keys to version control.** Ensure your API keys are kept confidential and secure.

## Running an Agent

To execute a specific agent:

1.  Navigate to the project root directory in your terminal.
2.  Run the agent's script using Python:

    ```bash
    python src/agents/<agent_name>.py
    ```

    Replace `<agent_name>` with the desired agent's filename (e.g., `whale_watcher_agent.py`).

## Documentation

Detailed documentation, including agent-specific guides and project architecture overviews, is located in the `docs/` directory.

## Roadmap

-   **Enhanced Agent Functionality:** Expand the capabilities of existing agents with more sophisticated strategies and features.
-   **New Agent Development:** Introduce new agents for additional DeFi tasks and opportunities.
-   **Improved Documentation:** Continuously update and expand project documentation for clarity and completeness.
-   **Community Contributions:** Encourage and integrate community contributions to broaden project scope and innovation.
-   **Integration with More DeFi Protocols:** Extend agent compatibility to a wider range of DeFi platforms and protocols.

## Contributing

We welcome contributions to the project! Please see `CONTRIBUTING.md` (to be created) for guidelines on how to contribute.

## License

This project is licensed under the MIT License.

## Disclaimer

**For Educational and Demonstration Purposes Only:** This project is intended for educational and demonstration purposes. It is not designed for production use or financial advice. Use of this project and its agents is at your own risk.
