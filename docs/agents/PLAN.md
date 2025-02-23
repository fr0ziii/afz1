# Enhancement Plan for FundingAgent

**Agent:** `src/agents/funding_agent.py`

**Objective:** Enhance the FundingAgent to improve configurability, robustness, and logging.

**Proposed Enhancements:**

1.  **Configurable Funding Rate Threshold:**
    *   Make the funding rate threshold configurable via the agent's configuration.
    *   This allows users to adjust the sensitivity of arbitrage opportunity detection.

2.  **Configurable Trading Pairs:**
    *   Allow users to specify trading pairs to monitor through the agent's configuration.
    *   This enables monitoring of different markets without code modifications.

3.  **Implement Slippage Control:**
    *   Introduce a slippage tolerance parameter in the configuration.
    *   Incorporate slippage control in trade execution to account for price fluctuations during order placement.

4.  **Configurable Spot Order Type:**
    *   Make the spot order type configurable (e.g., 'market', 'limit') in the agent's configuration.
    *   Provide flexibility in order execution based on user preferences and exchange capabilities.

5.  **Enhanced Logging:**
    *   Improve logging detail by adding timestamps, function parameters, and more context to log messages.
    *   Enhance traceability and debugging capabilities.

6.  **Improved Error Handling:**
    *   Refine error handling to differentiate between various error types (network, API, etc.).
    *   Log specific error details for better diagnostics and potential automated recovery.

**Implementation Steps:**

1.  **Configuration Updates:**
    *   Modify the agent's configuration schema to include:
        *   `funding_rate_threshold` (float)
        *   `trading_pairs` (list of strings)
        *   `slippage_tolerance` (float)
        *   `spot_order_type` (string)

2.  **Code Modifications:**
    *   `src/agents/funding_agent.py`:
        *   Modify `_identify_arbitrage_opportunities` to use `funding_rate_threshold` from config.
        *   Modify `_execute_arbitrage_trade` to:
            *   Incorporate `slippage_tolerance` in order placement logic.
            *   Use `spot_order_type` from config for spot orders.
        *   Enhance logging throughout the class.
        *   Refine error handling with more specific exception handling and logging.

3.  **Documentation Updates:**
    *   Update `docs/agents/funding_agent.md` to document the new configuration options and enhancements.

**Next Steps:**

*   Proceed with implementing the configuration updates and code modifications in `src/agents/funding_agent.py`.
*   Update documentation in `docs/agents/funding_agent.md`.
*   Test the enhanced FundingAgent with different configurations and market conditions.