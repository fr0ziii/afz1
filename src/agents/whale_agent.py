from src.agents.base_agent import BaseAgent

class WhaleAgent(BaseAgent):
    """
    Whale Agent for monitoring and analyzing whale trades and activities.

    This agent is responsible for:
    - Loading and validating whale agent configurations.
    - Setting up necessary dependencies for whale monitoring (e.g., API clients, data sources).
    - Implementing the core logic for detecting and analyzing whale trades and activities.
    - Generating alerts or notifications based on detected whale movements.
    - Handling graceful shutdown and stopping of whale monitoring operations.
    """

    def __init__(self, config: dict):
        """
        Initializes the WhaleAgent.

        Args:
            config (dict): Agent configuration parameters.
        """
        super().__init__(config)
        self.load_config(config) # Load and validate configuration
        self.setup_dependencies() # Setup agent dependencies
        # Initialize whale monitoring specific components here

    def load_config(self, config: dict) -> dict:
        """
        Loads and validates the WhaleAgent configuration.

        Args:
            config (dict): Configuration dictionary.

        Returns:
            dict: Validated configuration dictionary.

        Raises:
            ValueError: If configuration is invalid or missing required parameters.
        """
        if not isinstance(config, dict):
            raise ValueError("WhaleAgent config must be a dictionary")
        # Add whale-specific configuration loading and validation here
        return config

    def setup_dependencies(self):
        """
        Sets up WhaleAgent dependencies, such as API clients or data streams.
        """
        # Initialize any whale-specific dependencies here
        pass

    def run(self):
        """
        Executes the main whale monitoring logic of the agent.

        This method contains the core logic for monitoring and analyzing
        whale trades and activities. Subclasses should override this method
        to define their specific whale monitoring logic.
        """
        pass  # Implement whale monitoring logic here

    def stop(self):
        """
        Stops the whale agent and any ongoing operations gracefully.

        This method should handle the graceful shutdown of the whale agent,
        such as closing connections and releasing resources.
        """
        super().stop()
        # Implement graceful shutdown of whale agent here