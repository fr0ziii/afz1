# Web Interface Guide

This guide provides instructions on how to use the web-based user interface for the `afz1` project.

## Accessing the Web Interface

1.  **Start the Web Server:**
    Navigate to the `src/frontend/` directory in your terminal:

    ```bash
    cd src/frontend/
    ```

    Run the main frontend application script (assuming it's `main.py` based on file structure analysis):

    ```bash
    python main.py
    ```

    (Note: Specific command to start the web server might vary. Refer to project-specific instructions if available.)

2.  **Access in Browser:**
    Open your web browser and navigate to the address provided by the running web server (typically `http://127.0.0.1:5000` or `http://localhost:5000`, but may vary depending on configuration).

## Frontend Overview

The web interface provides a user-friendly way to interact with and monitor the `afz1` AI trading system. The main sections and functionalities typically include:

*   **Agent Dashboard:**
    *   Displays a list of available agents and their current status (running, stopped, error).
    *   Provides controls to start, stop, and restart agents.
    *   May show real-time performance metrics and key indicators for each agent.

*   **Agent Configuration Panel:**
    *   Allows users to configure parameters for individual agents.
    *   May include settings for trading pairs, risk parameters, AI model selection, data sources, and strategy selection.

*   **Data Visualization Dashboard:**
    *   Presents charts and graphs to visualize market data, agent performance, portfolio status, and other relevant information.
    *   May include interactive charts for OHLCV data, sentiment indicators, risk metrics, and backtesting results.

*   **Chat Interface (If Implemented):**
    *   Provides a chat-based interface to interact with agents or the system.
    *   Users may be able to ask questions, issue commands, or receive reports through the chat interface.

*   **System Monitoring:**
    *   Displays system-level metrics such as resource usage (CPU, memory), API connection status, and error logs.

## Using Agent Controls

*   **(Explain how to start, stop, and restart agents using the web interface elements - buttons, dropdowns, etc.)**
*   **(Explain how to configure agent parameters through the web interface forms or settings panels.)**

## Data Visualization and Monitoring

*   **(Describe the charts and dashboards available in the frontend, and how to interpret them. Explain what data is visualized and how to use the visualizations for monitoring agent performance and market conditions.)**

## Chat Interface Guide (If Applicable)

*   **(If a chat interface is implemented, provide instructions on how to use it. Explain available commands, types of questions to ask, and how to interpret responses from agents through the chat interface.)**

## Customization (Basic)

(If basic customization options are available within the web interface, provide brief guidance here. More advanced customization would typically involve modifying the frontend code directly.)

By using the web interface, users can effectively manage, monitor, and interact with the `afz1` AI trading system in a visually intuitive manner.
