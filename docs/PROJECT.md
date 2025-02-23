afz1 Project: File Structure and Specificationss
---------------------------------------------------------------------------

1\. Executive Summary

The `afz1` project is an open-source framework for developing and deploying AI-powered trading agents, specifically designed for cryptocurrency markets. The project features a modular, agent-centric architecture, integrating Large Language Models (LLMs) for advanced market analysis and trading strategy execution. Key functionalities include a diverse suite of trading agents, a market data API, a comprehensive backtesting framework, and a web-based user interface. This document outlines the project's file structure and specifications to facilitate understanding of its architecture and potential for further development.

2\. Project Purpose and Value Proposition

The primary purpose of `afz1` is to provide a robust, extensible platform for building and experimenting with AI-driven trading strategies in cryptocurrency markets. The project aims to democratize access to advanced algorithmic trading tools by offering a fully open-source solution. The value proposition includes:

-   Agent-Based Modularity: A highly modular architecture enabling users to leverage and customize specialized agents for various trading tasks.
-   AI-Powered Analysis: Integration of LLMs for sophisticated market analysis, sentiment assessment, and strategy development.
-   Comprehensive Toolset: Provides a complete ecosystem encompassing data acquisition, agent deployment, strategy backtesting, and user interface.
-   Open Source Accessibility: Offers a free and open-source platform, promoting community contribution and customization.

3\. Target Audience and Use Cases

The primary target audience for `afz1` includes:

-   Algorithmic Traders: Individuals and teams seeking to develop and automate cryptocurrency trading strategies using AI.
-   Quantitative Analysts: Professionals interested in leveraging AI for market analysis, backtesting, and research in crypto markets.
-   Developers: Software engineers and AI/ML practitioners looking to contribute to or build upon an open-source AI trading framework.
-   Educational Users: Students and researchers studying AI in finance and algorithmic trading.

Potential use cases include:

-   Automated Trading Strategy Execution: Deploying AI agents to execute predefined or dynamically generated trading strategies.
-   Market Monitoring and Alerting: Utilizing agents to monitor market conditions, identify trading opportunities, and generate alerts.
-   Backtesting and Strategy Development: Leveraging the backtesting framework to research, develop, and validate new trading strategies.
-   AI-Driven Market Research: Employing agents for sentiment analysis, news monitoring, and fundamental analysis to inform trading decisions.
-   Educational Platform: Using the project as a learning tool to understand AI in finance and algorithmic trading.

4\. File Structure Overview

The project's file structure is organized to promote modularity and maintainability. The top-level directory `afz1/` contains the following key subdirectories and files:

```
afz1/
├── docs/              # Project documentation (API, examples)
├── src/               # Source code
│   ├── agents/        # AI Agent implementations
│   ├── data/          # Data management and storage
│   ├── frontend/      # Web frontend components
│   ├── models/        # AI Model integrations and factory
│   ├── scripts/       # Utility and experimental scripts
│   ├── strategies/    # Trading strategies and base classes
│   ├── web/           # Web-related components (chat interface)
│   ├── config.py      # Project configuration
│   ├── ezbot.py       # Core bot/utility module (TBD)
│   ├── main.py        # Main entry point for execution
│   ├── nice_funcs.py  # Utility functions
│   ├── nice_funcs_hl.py # HyperLiquid/High-Level utility functions
│   └── __init__.py    # Initializes src/ as a Python package
├── README.md          # Project overview and documentation links
├── requirements.txt   # Python dependencies
└── .cursorrules       # IDE configuration rules

```

5\. Key Components and Specifications

5.1. Source Code Directory (`src/`)

-   Agents (`src/agents/`):

    -   Purpose: Contains implementations for all AI trading agents. Agent-centric architecture emphasizes specialized modules for distinct trading-related tasks.
    -   Key Files:
        -   `api.py`: Market Data API client for accessing real-time and historical market data.
        -   `base_agent.py`: Abstract base class defining the agent interface and common functionalities.
        -   Agent-specific files (`chartanalysis_agent.py`, `trading_agent.py`, etc.): Implementations for individual agents, each focused on a specific task (chart analysis, trading, risk management, sentiment analysis, etc.).
        -   `model_factory.py`: Factory pattern for instantiating and managing different AI models (Claude, DeepSeek, Gemini, Groq, Ollama, OpenAI).
    -   Specifications:
        -   Modular design for agent specialization and extensibility.
        -   Integration with `model_factory.py` for flexible AI model selection.
        -   `base_agent.py` promotes code reusability and consistent agent structure.
-   Data Management (`src/data/`):

    -   Purpose: Manages data collection, storage, and organization for the project.
    -   Key Files and Subdirectories:
        -   CSV data files: Storage for agent outputs, historical market data (funding, liquidations, open interest, sentiment), backtesting results, and portfolio information.
        -   `ohlcv_collector.py`: Script for collecting OHLCV market data.
        -   `rbi/backtests/`: Comprehensive backtesting framework with scripts for various trading strategies, performance statistics, and generated charts.
        -   `coingecko_results/`, `code_runner/`, `tweets/`, `videos/`: Subdirectories for organizing data by source or agent type.
    -   Specifications:
        -   CSV-based data storage for simplicity and accessibility.
        -   Organized directory structure for different data types and sources.
        -   Includes data collection scripts and backtesting data management.
-   Models (`src/models/`):

    -   Purpose: Houses integrations for various Large Language Models (LLMs) and the `model_factory`.
    -   Key Files:
        -   `base_model.py`: Abstract base class for AI model integrations.
        -   Model-specific files (`claude_model.py`, `deepseek_model.py`, etc.): Implementations for integrating specific LLMs, handling API interactions and model configurations.
        -   `model_factory.py`: Factory class for creating and managing AI model instances, enabling runtime model selection.
    -   Specifications:
        -   Modular design for easy integration of new AI models.
        -   Abstraction through `base_model.py` for consistent model interface.
        -   Supports a range of LLMs (Claude, DeepSeek, Gemini, Groq, Ollama, OpenAI).
-   Strategies (`src/strategies/`):

    -   Purpose: Provides a framework for defining and implementing trading strategies, including base classes and examples.
    -   Key Files:
        -   `base_strategy.py`: Abstract base class for defining trading strategy interfaces and common methods.
        -   `example_strategy.py`: Example strategy implementation.
        -   `custom/`: Subdirectory for user-defined, custom trading strategies.
    -   Specifications:
        -   Strategy implementations are modular and inherit from `base_strategy.py`.
        -   Users can create custom strategies within the `custom/` subdirectory.
-   Web Interface (`src/frontend/` and `src/web/`):

    -   Purpose: Provides web-based user interfaces for interacting with and monitoring the AI trading system.
    -   Key Directories:
        -   `frontend/`: Primary web frontend, likely built with Flask, for user interaction and agent management. Includes HTML templates, CSS, JavaScript, and static assets.
        -   `web/`: Contains `chat_interface.py`, suggesting a web-based chat interface, possibly built with Streamlit.
    -   Specifications:
        -   Frontend likely supports agent control, data visualization, and system monitoring.
        -   Potential integration with Twilio for phone call functionalities (based on dependencies and configuration files).
-   Scripts (`src/scripts/`):

    -   Purpose: Contains utility and experimental scripts for development, testing, and data manipulation.
    -   Key Files: Scripts for CoinGecko API examples, DeepSeek model interactions, backtesting utilities, funding rate arbitrage calculations, token list management, Twitter API login, and other development-related tasks.
    -   Specifications:
        -   Provides helpful tools for development, testing, and data analysis.
        -   Includes scripts for interacting with external APIs and services.

5.2. Top-Level Files

-   `main.py`: The primary execution script, responsible for system initialization, agent orchestration, and running the trading system.
-   `requirements.txt`: Lists all Python dependencies, ensuring environment reproducibility.
-   `.cursorrules`: IDE-specific configuration file for development guidelines.

6\. Development Status and Roadmap

The project is currently in alpha and is under active development. Key features are being continuously added and refined. Future development may include:

-   Enhanced agent functionalities and new agent types.
-   Improved web interface with more comprehensive monitoring and control features.
-   Expanded documentation and examples.
-   Further optimization of backtesting and strategy development tools.
-   Community contributions and feature requests.

7\. Disclaimers and Important Notes

-   Experimental Project: This is an experimental research project and not a production-ready trading system.
-   No Financial Guarantees: There are no guarantees of profitability, and trading involves substantial risk of loss.
-   User Responsibility: Users are responsible for understanding the code, developing and validating their own trading strategies, and managing risk appropriately.
-   No Financial Advice: The project is for educational and informational purposes only and does not constitute financial advice.

This revised document provides a more structured and detailed overview of the `afz1` project, suitable for review from a product management perspective. It emphasizes the project's architecture, functionalities, and key specifications, while also highlighting its development status and important disclaimers.