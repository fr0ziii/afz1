<h1 style="text-align: center;"> afz1 - Autonomous Finance Agents </h1>

afz1 is a project focused on developing autonomous agents for various tasks in the decentralized finance (DeFi) space. These agents are designed to automate and optimize different aspects of trading, risk management, information gathering, and more.

## Project Structure

The project is structured as follows:

-   `src/`: Contains the source code for the different autonomous agents.
-   `.env_example`: Example environment file.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `README.md`: The current file, providing an overview of the project.
-   `requirements.txt`: Lists the project's dependencies.

## Agents

The `src/agents/` directory contains a variety of agents, each designed for a specific purpose:

-   `base_agent.py`: Base class for all agents.
-   `chartanalysis_agent.py`: Agent for analyzing charts.
-   `chat_agent.py`: Agent for interacting with chat platforms.
-   `clips_agent.py`: Agent for creating video clips.
-   `code_runner_agent.py`: Agent for running code.
-   `copybot_agent.py`: Agent for copying trading strategies.
-   `focus_agent.py`: Agent for focusing on specific tasks.
-   `funding_agent.py`: Agent for managing funding.
-   `fundingarb_agent.py`: Agent for arbitrage in funding markets.
-   `liquidation_agent.py`: Agent for monitoring liquidations.
-   `listingarb_agent.py`: Agent for arbitrage in listing markets.
-   `new_or_top_agent.py`: Agent for identifying new or top assets.
-   `phone_agent.py`: Agent for interacting with phone services.
-   `rbi_agent.py`: Agent for regulatory compliance.
-   `risk_agent.py`: Agent for managing risk.
-   `sentiment_agent.py`: Agent for analyzing sentiment.
-   `sniper_agent.py`: Agent for sniping trades.
-   `solana_agent.py`: Agent for interacting with the Solana blockchain.
-   `trading_agent.py`: Agent for executing trades.
-   `tweet_agent.py`: Agent for interacting with Twitter.
-   `tx_agent.py`: Agent for monitoring transactions.
-   `video_agent.py`: Agent for creating videos.
    -   `whale_agent.py`: Agent for monitoring large transactions (whales).
-   `whale_watcher_agent.py`: Agent for monitoring large transactions (whales).

## Setup and Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/fr0ziii/afz1
    cd afz1
    ```
2.  **Environment Setup:**

    Navigate into the cloned `afz1` directory in your terminal.

    *   **Using venv (Example):**

        ```bash
        python3.10 -m venv venv
        source venv/bin/activate   # On Linux/macOS
        venv\Scripts\activate  # On Windows
        ```
3.  **Dependency Installation:**

    Install the required Python packages listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
4.  **API Keys Configuration:**

    *   Copy the `.env_example` file to `.env`:

        ```bash
        cp .env_example .env  # On Linux/macOS
        copy .env_example .env  # On Windows
        ```
    *   Open the `.env` file and add your API keys:

        ```
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        BINANCE_API_KEY=YOUR_BINANCE_API_KEY
        # Add other API keys as needed
        ```

    **Important Security Note:** Never commit the `.env` file with your actual API keys to version control. Keep your API keys secure.

## Running an Agent

To run a specific agent, navigate to the project directory and execute the agent's script using Python:

```bash
python src/agents/<agent_name>.py
```

Replace `<agent_name>` with the name of the agent you want to run (e.g., `whale_watcher_agent.py`).

## Documentation

Detailed documentation for each agent and the project as a whole can be found in the `docs/` directory.

## Contributing

Contributions to the project are welcome. Please refer to the contributing guidelines for more information.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is for demonstration and educational purposes only. It is not intended for production use or financial advice. Use it at your own risk.
