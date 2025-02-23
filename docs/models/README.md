# Model Guide

This guide documents the AI model integrations and the `model_factory` component within the `afz1` project.

## Model Factory (`src/agents/model_factory.py`)

The `afz1` project utilizes a Model Factory pattern implemented in `src/agents/model_factory.py` to manage and instantiate different Large Language Models (LLMs). This design provides flexibility and allows for easy switching between various AI models without modifying agent code directly.

*   **Purpose:**
    *   Abstracts the process of creating AI model instances.
    *   Supports multiple LLM providers (Claude, DeepSeek, Gemini, Groq, Ollama, OpenAI).
    *   Simplifies model configuration and selection within agents.
    *   Promotes modularity and extensibility for adding new model integrations.

*   **Supported Models:**
    *   **Claude:** (Link to Claude API documentation if available)
    *   **DeepSeek:** (Link to DeepSeek API documentation if available)
    *   **Gemini:** (Link to Gemini API documentation if available)
    *   **Groq:** (Link to Groq API documentation if available)
    *   **Ollama:** [ollama.com](https://ollama.com/) (For local model execution)
    *   **OpenAI:** [platform.openai.com](https://platform.openai.com/)

*   **Model Implementation Files (`src/models/`)**:
    *   Each supported AI model has a corresponding implementation file in the `src/models/` directory (e.g., `claude_model.py`, `deepseek_model.py`, `gemini_model.py`, `groq_model.py`, `ollama_model.py`, `openai_model.py`).
    *   These files contain classes that inherit from `base_model.py` and implement the specific API interactions and configurations for each LLM provider.

*   **`base_model.py`**:
    *   Defines the abstract `BaseModel` class in `src/models/base_model.py`.
    *   Provides a common interface that all model implementations must adhere to, ensuring consistency across different LLM integrations.

## Model Configuration

Model-specific configurations, such as API keys and model names, are typically handled through environment variables or configuration files. Refer to the Setup Guide and agent-specific documentation for details on configuring models.

## Model Selection Strategies

When choosing an AI model for a specific agent or task, consider the following factors:

*   **Model Capabilities:**  Different LLMs have varying strengths in areas like text generation, reasoning, code generation, and language understanding. Choose a model that aligns with the agent's requirements.
*   **Performance and Latency:**  Consider the processing speed and latency of different models, especially for time-sensitive trading applications.
*   **Cost:**  LLM APIs have different pricing models. Evaluate the cost implications of using different models, especially for high-frequency agent usage.
*   **Availability and Reliability:**  Consider the availability and reliability of the LLM API provider.
*   **Local vs. Cloud Models:**  Ollama allows for running models locally, offering privacy and potentially lower latency but requiring local computational resources. Cloud-based APIs offer scalability but depend on network connectivity and external service availability.

## Adding New Models

Developers can extend the `afz1` project by integrating new AI models. To add a new model:

1.  **Create a New Model Implementation File:**
    In `src/models/`, create a new Python file (e.g., `new_model.py`) for your model integration.

2.  **Implement a Class Inheriting from `BaseModel`:**
    In your new file, create a class that inherits from `BaseModel` and implement the necessary methods to interact with the new model's API.

3.  **Integrate into `model_factory.py`:**
    Modify the `model_factory.py` to include your new model in the factory's model selection logic.

4.  **Configure Agent to Use New Model:**
    Update agent configurations to specify the use of your newly integrated model (refer to Agent Guide).

By leveraging the Model Factory and understanding the model integration structure, developers can easily experiment with different AI models and extend the capabilities of the `afz1` project.
