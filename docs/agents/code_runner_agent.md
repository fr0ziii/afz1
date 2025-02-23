# Code Runner Agent

## Description

The Code Runner Agent is designed for executing and testing code snippets. It provides a basic framework for agents that can run code dynamically, allowing for tasks such as backtesting strategies, executing custom scripts, or integrating with external APIs programmatically. This agent is useful for users who need to execute and manage code within the afz1 framework.

## Missions

[Description of the missions this agent is designed to accomplish. Link to mission files if applicable.]
- Currently, no specific mission files are defined for the Code Runner Agent. Missions would be defined based on the type of code to be executed and the purpose of execution (e.g., backtesting, data analysis).

## Configuration

The Code Runner Agent inherits basic configuration parameters from the `BaseAgent`. Specific configurations for code execution environments, supported languages, and security settings would be defined in the agent's configuration.

-   **agent_id**: A unique identifier for the agent instance.
-   **agent_type**: Must be set to `CodeRunnerAgent`.

### Example Configuration

```yaml
config:
  agent_id: code_runner_agent_01
  agent_type: CodeRunnerAgent
  # Add any code execution specific configurations here in the future
```

## Inputs and Outputs

### Inputs

-   **Code Snippets**: Code snippets to be executed, provided as strings or file paths.
-   **Execution Environment Configuration**: Parameters defining the execution environment (e.g., language, libraries, runtime).

### Outputs

-   **Execution Results**: Output from the executed code, including standard output and error streams.
-   **Logs**: Informational and error logs for monitoring agent activity and debugging.

## Workflow

1.  **Receive Code**: The agent receives code snippets to be executed, along with any execution environment configurations.
2.  **Execute Code**: The agent executes the provided code in a controlled environment (currently placeholder logic).
3.  **Capture Output**: The agent captures the output from the code execution, including any errors or logs (currently placeholder logic).
4.  **Return Results**: The agent returns the execution results to the user or calling process.
5.  **Log Execution**: The agent logs the code execution process and results for monitoring and analysis.

## Example Usage

To run the Code Runner Agent, you would instantiate and run the agent, providing the code to be executed as input. Since the current implementation is basic, the example usage primarily involves setting up the agent and potentially adding code execution logic.

```python
from src.agents.code_runner_agent import CodeRunnerAgent

config = {
  "agent_id": "code_runner_agent_01",
  "agent_type": "CodeRunnerAgent",
}

agent = CodeRunnerAgent(config)
# agent.run() # Run method currently placeholder
# Example of providing code for execution (to be implemented)
# code_snippet = "print('Hello, world!')"
# results = agent.run_code(code_snippet)
# print(results)
```

This example shows the basic instantiation of the Code Runner Agent. The `run` method is currently a placeholder and would need to be implemented with actual code execution logic.  Future implementations would include methods to pass code snippets to the agent for execution.

## Code Location

-   `src/agents/code_runner_agent.py`

## Components

-   **`src/agents/base_agent.py` (BaseAgent)**: The Code Runner Agent inherits basic agent functionalities from the `BaseAgent`.
-   **Code Execution Components (To be implemented)**: Future implementations would include components for secure code execution, language runtimes, and library management.
-   **Input/Output Handling Components (Future)**: Components to handle input of code snippets and output of execution results.

## Notes and Considerations

-   **Placeholder Implementation**: The current `CodeRunnerAgent` is a basic placeholder. Significant implementation is required to add actual code execution capabilities.
-   **Security**:  Security is a critical consideration for a Code Runner Agent. Implementations must ensure secure code execution environments to prevent malicious code from harming the system.
-   **Supported Languages**:  Define the programming languages supported by the agent (e.g., Python, JavaScript, etc.) and configure the execution environment accordingly.
-   **Resource Management**:  Implement resource management to limit the resources consumed by executed code and prevent resource exhaustion.
-   **Error Handling**: Robust error handling is needed to manage code execution errors and provide informative feedback to users.