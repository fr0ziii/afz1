from abc import ABC, abstractmethod
import logging

class BaseAgent(ABC):
    """
    Abstract base class for all agents in the afz1 project.

    Defines the common interface, attributes, and functionalities
    for all agent implementations. Subclasses should inherit from this
    class and implement the abstract methods.
    """

    def __init__(self, config: dict):
        """
        Initializes the BaseAgent with a configuration dictionary.

        Args:
            config (dict): Agent configuration parameters.
                           This dictionary will be accessible throughout the agent.
        """
        self.config = self.load_config(config) # Load and validate configuration
        self.logger = logging.getLogger(self.__class__.__name__)
        self.status = "initialized"  # Agent status: initialized, running, stopped, error
        self.setup_dependencies() # Setup agent dependencies

    def load_config(self, config: dict) -> dict:
        """
        Loads and validates the agent configuration.

        This method is responsible for loading the agent's configuration
        from the provided dictionary and performing any necessary validation.
        Subclasses can override this method to implement custom
        configuration loading and validation logic, such as loading
        from environment variables or configuration files.

        Args:
            config (dict): Configuration dictionary passed to the constructor.

        Returns:
            dict: The validated configuration dictionary.
                  In the BaseAgent, it simply returns the input config as is.
        """
        # In base class, simply return the config.
        # Subclasses can override to add validation or load from other sources.
        return config

    @abstractmethod
    def setup_dependencies(self):
        """
        Abstract method to define the setup of agent dependencies.

        This method is responsible for initializing any resources,
        API clients, or other dependencies required by the agent
        to function properly. Subclasses must implement this method
        to ensure all necessary dependencies are set up before the agent
        starts running. Examples include:

        - Initializing API clients (e.g., for exchanges or LLMs)
        - Connecting to databases or data streams
        - Loading models or other resources

        Subclasses should implement the dependency setup logic here.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Abstract method to define the main execution logic of the agent.
        Subclasses must implement this method.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Abstract method to define how to stop the agent gracefully.
        Subclasses must implement this method.
        """
        self.status = "stopped"

    def get_status(self):
        """
        Returns the current status of the agent.
        """
        return self.status

    def _set_status(self, status: str):
        """
        Updates the agent's status. Should be used internally by agent implementations.
        """
        if status not in ["initialized", "running", "stopped", "error"]:
            raise ValueError(f"Invalid agent status: {status}")
        self.status = status
        self.logger.info(f"Agent status updated to: {self.status}")

    def _log_info(self, message: str):
        """
        Logs an info message with the agent's logger.
        """
        self.logger.info(message)

    def _log_error(self, message: str, exc_info=False):
        """
        Logs an error message with the agent's logger.
        """
        self.logger.error(message, exc_info=exc_info)