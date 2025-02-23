# Code Runner Agent (`code_runner_agent.py`)

## Purpose

The Code Runner Agent is designed to provide a secure, isolated, and flexible environment for executing and testing code snippets within the `afz1` project. This agent is crucial for various development, testing, and utility tasks, offering benefits such as:

*   **Backtesting and Strategy Validation:** Allows users to run backtesting scripts or strategy evaluation code snippets to validate trading strategies and agent performance without needing to set up separate backtesting environments.
*   **Data Analysis and Exploration:** Enables execution of data analysis scripts for exploring market data, agent outputs, or other project-related datasets, facilitating data-driven insights and debugging.
*   **Utility Script Execution:** Provides a convenient way to run utility scripts, data manipulation tasks, or experimental code snippets within the `afz1` environment without directly altering the core system or requiring manual script execution in separate terminals.
*   **Rapid Prototyping and Experimentation:** Facilitates rapid prototyping and experimentation with new code ideas, algorithms, or data processing techniques in a controlled and easily accessible manner.
*   **Integration with Other Agents:** Can be used by other agents within the `afz1` system to dynamically execute code for specific tasks, enhancing the flexibility and adaptability of the agent ecosystem.

By providing a secure and sandboxed code execution environment, the Code Runner Agent enhances the development workflow, testing capabilities, and overall flexibility of the `afz1` project.

## Functionality

The Code Runner Agent is envisioned to provide the following key functionalities in future implementations:

*   **Secure and Isolated Code Execution:**
    - Execute user-provided code snippets in a secure and isolated environment, preventing unauthorized access to system resources or the core `afz1` codebase.
    - Implement sandboxing techniques (e.g., containerization, virtual machines, restricted execution environments) to enhance security.
*   **Multi-Language Support:**
    - Support execution of code snippets in multiple programming languages, catering to diverse user needs and tasks.
    - Initially focus on Python support due to its relevance in data science, machine learning, and the `afz1` project's codebase.
    - Future support for languages like JavaScript, R, or other scripting languages based on user demand.
*   **Flexible Code Input Methods:**
    - Allow users to provide code snippets as input through various methods, such as:
      - **Text Input:** Directly entering code snippets as text commands or through a user interface.
      - **File Upload:** Uploading code snippets from files (e.g., Python scripts, data files).
      - **Integration with Other Agents:** Receiving code snippets dynamically from other agents within the `afz1` system.
*   **Output Capture and Redirection:**
    - Capture and manage the output of executed code, including standard output (stdout) and standard error (stderr) streams.
    - Provide mechanisms to redirect or store the output for review, analysis, or integration with other agents/components.
*   **Resource Management and Control:**
    - Implement resource limits and monitoring to control the resources consumed by executed code, preventing resource exhaustion or denial-of-service issues.
    - Configure limits for execution time, memory usage, CPU usage, and network access.
*   **Execution Environment Configuration:**
    - (Future) Allow users to configure the execution environment for code snippets, such as:
      - Specifying language versions (e.g., Python 3.8, Python 3.9).
      - Selecting pre-installed libraries or packages.
      - Setting environment variables.
*   **Secure API and Access Control:**
    - Implement secure APIs and access control mechanisms to manage code execution requests and ensure authorized usage of the Code Runner Agent.
    - (Future) User authentication and authorization to control who can execute code and with what privileges.

## AI Model(s) Used

While the current implementation does not directly integrate AI models, future enhancements of the Code Runner Agent could leverage AI for several purposes:

*   **Code Analysis and Security Scanning:**
    - **Static Code Analysis Models:** Integrate static analysis tools or AI models (e.g., linters, code vulnerability scanners) to automatically analyze user-provided code snippets for potential security risks, vulnerabilities, or errors before execution.
    - **Security Policy Enforcement:** Use AI-powered policy enforcement mechanisms to ensure that executed code adheres to predefined security guidelines and resource limits.
*   **AI-Assisted Code Generation and Completion:**
    - **Code Completion Models:** Integrate code completion models (e.g., CodeBERT, GPT-Codex) to assist users in writing code snippets by providing intelligent code suggestions and autocompletion features within the Code Runner Agent interface.
    - **Code Generation from Natural Language:**  Utilize LLMs to generate code snippets from natural language descriptions or user intents, simplifying the process of writing utility scripts or data analysis code.
*   **Automated Test Case Generation and Validation:**
    - **Test Case Generation Models:** Employ AI models to automatically generate test cases for user-provided code snippets, ensuring code reliability and correctness.
    - **Output Validation:** Use AI-powered output validation techniques to automatically compare the output of executed code against expected results or predefined criteria, streamlining the testing and validation process.
*   **Code Optimization and Performance Analysis:**
    - **Performance Analysis Tools:** Integrate AI-driven performance analysis tools to profile and analyze the execution performance of code snippets, identifying potential bottlenecks or areas for optimization.
    - **Code Optimization Suggestions:**  Utilize AI models to provide suggestions for optimizing code snippets for better performance, resource utilization, or efficiency.

## Data Inputs

*   **Code Snippets:** Receives code snippets as input, typically as strings or files.
*   **Execution Environment Configurations (Future):**  Future versions may allow users to configure the execution environment (e.g., language version, libraries).

## Configuration Parameters

*   **agent\_id**: A unique identifier for the agent instance.
*   **agent\_type**: Must be set to `CodeRunnerAgent`.

### Example Configuration (YAML)

```yaml
config:
  agent_id: code_runner_agent_01
  agent_type: CodeRunnerAgent
```

## Example Usage

To instantiate and run the `CodeRunnerAgent`:

```python
from src.agents.code_runner_agent import CodeRunnerAgent

config = {
    "agent_id": "code_runner_agent_01",
    "agent_type": "CodeRunnerAgent",
}

agent = CodeRunnerAgent(config)
agent.run()
```

**Note:** The current implementation of `CodeRunnerAgent` provides a basic framework. To add actual code execution capabilities, you would need to extend the `CodeRunnerAgent` class and implement the following:

1.  **Code Execution Engine:** Integrate a code execution engine for the target language (e.g., Python's `exec` or `subprocess` for running scripts in a separate process).
2.  **Security Sandbox:** Implement a security sandbox to isolate code execution and prevent access to sensitive system resources. Consider using libraries like `restrictedpython` or containerization technologies.
3.  **Input Handling:** Implement secure and flexible methods for receiving code snippets as input (e.g., from chat commands, files, or APIs).
4.  **Output Capture and Management:** Capture and manage the output of executed code, including stdout, stderr, and return values.
5.  **Error Handling:** Implement robust error handling for code execution failures and security violations.

## Output and Monitoring

*   **Execution Results:**  Outputs the results of code execution, including stdout, stderr, and return values.
*   **Execution Logs:**  Logs details of code execution, including input code, execution time, and any errors or security violations.

## Customization Notes

*   **Extend for Multiple Languages:**  Customize the agent to support code execution in multiple programming languages by integrating different language-specific execution engines.
*   **Implement Security Policies:**  Define and enforce security policies for code execution, such as resource limits, allowed libraries, and access control.
*   **Integrate with Other Agents:**  The `CodeRunnerAgent` can be used by other agents in the `afz1` system to execute dynamic code for tasks like strategy backtesting or data analysis.
*   **User Interface for Code Input:**  Develop user interfaces (e.g., web UI, chat commands) to allow users to easily provide code snippets and execute them using the agent.

## Code Location

*   `src/agents/code_runner_agent.py`

## Components

*   **BaseAgent (`src/agents/base_agent.py`):**  The `CodeRunnerAgent` class inherits from `BaseAgent`, providing the basic agent lifecycle methods and configuration loading.

## Next Steps for Development

*   **Choose Code Execution Engine:** Select a suitable code execution engine for the target language (initially Python).
*   **Implement Basic Code Execution:** Implement the core logic to execute code snippets and capture output.
*   **Develop Security Sandbox:**  Integrate a security sandbox to isolate code execution and mitigate security risks.
*   **Add Input Handling and Output Management:** Implement methods for receiving code input and managing execution results.
*   **Enhance Error Handling and Logging:** Implement robust error handling and logging for code execution.