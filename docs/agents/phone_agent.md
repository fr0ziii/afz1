# Phone Agent (`phone_agent.py`)

## Purpose

The Phone Agent is designed to integrate voice-based communication into the `afz1` project, enabling real-time phone call interactions and delivery of critical voice notifications or alerts to users. In time-sensitive trading scenarios, phone call alerts can provide a direct and immediate communication channel, ensuring users do not miss important events. The Phone Agent aims to offer the following benefits:

*   **Critical Alert Delivery via Voice:**  Provide a highly reliable and immediate channel for delivering critical trading alerts, risk notifications, or urgent market updates directly to users via phone calls, ensuring immediate attention even when users are away from their screens.
*   **Hands-Free Interaction:** Enable hands-free interaction with the `afz1` system through voice commands and voice-based information retrieval, offering a convenient and accessible way to manage agents or receive updates, especially in mobile or multitasking scenarios.
*   **Enhanced Accessibility:**  Improve accessibility for users who may prefer voice-based interfaces or have visual impairments, providing an alternative communication channel to complement text-based interfaces.
*   **Interactive Voice Response (IVR) System Potential:**  Lay the foundation for implementing more advanced Interactive Voice Response (IVR) systems in the future, allowing users to interact with the `afz1` platform through voice menus, voice commands, and conversational voice interactions.
*   **Emergency Communication Channel:**  Serve as a reliable emergency communication channel to reach users in case of critical system errors, security alerts, or urgent account-related notifications, ensuring timely awareness and response to critical issues.

By integrating phone call functionalities, the Phone Agent aims to enhance the immediacy, accessibility, and reliability of critical communication within the `afz1` trading ecosystem.

## Functionality

The Phone Agent, in its advanced form, is expected to provide a rich set of functionalities for voice-based communication:

*   **Outbound Voice Notifications and Alerts:**
    - **Automated Outbound Calls:**  Initiate automated outbound phone calls to user-defined phone numbers to deliver critical trading alerts, risk notifications, or urgent market updates in real-time.
    - **Text-to-Speech (TTS) Integration:**  Convert text-based alerts, reports, or summaries into natural-sounding voice notifications using integrated Text-to-Speech (TTS) engines for voice delivery over phone calls.
    - **Customizable Alert Messages:**  Allow users to customize the content and format of voice alert messages to ensure clarity and relevance of phone call notifications.
*   **Interactive Voice Response (IVR) for Inbound Call Handling:**
    - **Voice Command Recognition:**  Implement Speech-to-Text (STT) and Natural Language Understanding (NLU) capabilities to enable the agent to understand and process user voice commands received via inbound phone calls.
    - **Voice-Based Agent Control:**  Allow users to control basic agent functions or request information from the `afz1` system using voice commands over the phone (e.g., "Pause trading agent", "What is my portfolio risk level?", "Summarize market news").
    - **Interactive Voice Menus and Navigation:**  Develop interactive voice menus and navigation systems to guide users through different options and functionalities via phone calls, enabling voice-based interaction with the `afz1` platform.
*   **Telephony Service and Communication Management:**
    - **Telephony API Integration:**  Seamlessly integrate with leading telephony service providers (e.g., Twilio, Vonage, Plivo) via their APIs to handle call initiation, call routing, call management, and SMS functionalities.
    - **Call Logging and History Tracking:**  Maintain detailed logs of all inbound and outbound phone calls, including call duration, status, timestamps, and any errors or issues encountered, facilitating monitoring and debugging.
    - **Call Scheduling and Queuing:** (Future) Implement call scheduling and queuing mechanisms to manage outbound call volumes efficiently and prioritize critical alerts during peak periods or for large user bases.

## AI Model(s) Used

Future implementations of the Phone Agent could significantly benefit from integrating AI models to enable advanced voice-based interactions:

*   **Text-to-Speech (TTS) for Voice Notifications:**
    - **High-Quality TTS Engines:**  Utilize advanced Text-to-Speech (TTS) models (e.g., Google Cloud TTS, Amazon Polly, Microsoft Azure TTS, open-source models like Mozilla TTS) to generate natural-sounding and high-quality voice notifications for delivery via phone calls.
    - **Customizable Voices and Languages:**  Leverage TTS models that offer a variety of voices, accents, and language support to personalize voice notifications and cater to diverse user preferences and localization needs.
*   **Speech-to-Text (STT) for Voice Command Recognition:**
    - **Real-time STT Models:**  Integrate real-time Speech-to-Text (STT) models (e.g., Google Cloud STT, AssemblyAI, DeepSpeech) to accurately transcribe user voice input from inbound phone calls into text, enabling voice command recognition and natural language interaction.
    - **Noise Robustness and Accent Handling:**  Employ STT models that are robust to background noise and can effectively handle different accents and speech patterns for reliable voice command processing in real-world environments.
*   **Natural Language Understanding (NLU) for Intent Recognition:**
    - **NLU Models for Command Parsing:**  Utilize Natural Language Understanding (NLU) models (e.g., Rasa NLU, Dialogflow, spaCy) to analyze transcribed user voice input and accurately identify user intents, commands, and relevant entities for voice-based agent control and IVR interactions.
    - **Contextual Understanding and Dialogue Management:**  Implement NLU models that can maintain conversation context and manage multi-turn dialogues with users via voice, enabling more natural and interactive voice-based communication.
*   **Voice Biometrics and User Authentication:**
    - **Voice Biometric Models:**  Explore voice biometric models for user authentication and security, allowing users to securely access agent functionalities or confirm transactions via voice recognition during phone calls.
    - **Speaker Verification and Identification:**  Utilize speaker verification and identification models to enhance security and personalize voice interactions based on individual user voice profiles.

## Data Inputs

The Phone Agent's functionality is driven by the following data inputs:

*   **Event Triggers for Outbound Calls:**
    - **Agent-Generated Alerts:**  Alerts generated by other agents within the `afz1` system that require immediate voice notification (e.g., critical trading signals from `ChartAnalysisAgent`, risk level breaches from `RiskAgent`, liquidation alerts from `LiquidationAgent`).
    - **User-Defined Alerts:**  User-configured alerts based on specific market conditions, price levels, or time-based triggers that should result in phone call notifications.
    - **System Events:**  Critical system events or errors that require immediate user attention and voice-based notification for prompt response and troubleshooting.
*   **User Voice Input for Inbound Calls (Future):**
    - **Voice Commands:**  User voice commands received during inbound phone calls, intended for agent control, information retrieval, or IVR interactions.
    - **Spoken Queries:**  User voice queries or questions related to market data, agent status, or account information, requiring voice-based responses from the agent.
*   **Configuration Parameters:**
    - **Telephony Service API Credentials:**  Securely configured API keys and authentication tokens for integrating with the chosen telephony service provider (e.g., Twilio, Vonage).
    - **User Phone Numbers:**  User-defined phone numbers for initiating outbound calls and routing inbound calls.
    - **Voice Notification Preferences:**  User preferences for voice notification types, alert categories, notification schedules, and preferred languages or voices for TTS.
    - **IVR System Configuration:** (Future) Configuration settings for defining voice menus, IVR flows, and voice command mappings for interactive voice response functionalities.

## Configuration Parameters

*   **agent\_id**: A unique identifier for the agent instance.
*   **agent\_type**: Must be set to `PhoneAgent`.

### Example Configuration (YAML)

```yaml
config:
  agent_id: phone_agent_01
  agent_type: PhoneAgent
```

## Example Usage

To instantiate and run the `PhoneAgent`:

```python
from src.agents.phone_agent import PhoneAgent

config = {
    "agent_id": "phone_agent_01",
    "agent_type": "PhoneAgent",
}

agent = PhoneAgent(config)
agent.run()
```

**Note:** The current implementation of `PhoneAgent` provides a basic framework. To add actual phone call interaction capabilities, you would need to extend the `PhoneAgent` class and implement the following:

1.  **Telephony Service Integration:** Integrate with a telephony service API (e.g., Twilio, Vonage) to handle call initiation, call reception, and voice communication.
2.  **Outbound Call Logic:** Implement logic to trigger outbound phone calls based on specific events or alerts.
3.  **Voice Notification Implementation:** Integrate a Text-to-Speech (TTS) engine to convert text alerts into voice notifications for delivery via phone calls.
4.  **(Optional) Inbound Call Handling:** Implement logic to handle inbound phone calls, potentially using Speech-to-Text (STT) and Natural Language Understanding (NLU) for voice command recognition or IVR interactions.
5.  **User Interface for Phone Configuration:**  Develop user interfaces (e.g., web UI, chat commands) to allow users to configure phone numbers, notification preferences, and telephony service settings.

## Output and Monitoring

*   **Phone Call Notifications (Future):**  In future implementations, the agent will initiate phone calls to deliver voice notifications or alerts.
*   **(Future) Phone Call Interactions:**  For inbound call handling, the agent will manage interactive voice responses or voice command processing.
*   **Call Logs:**  Logs of initiated or received phone calls, call status, and any errors encountered.

## Customization Notes

*   **Integrate with Specific Telephony Services:**  Customize the agent to work with a specific telephony service API of your choice.
*   **Implement Different Notification Types:**  Extend the agent to deliver various types of voice notifications, such as critical alerts, market summaries, or agent status updates.
*   **Develop Interactive Voice Response (IVR) Features:**  For more advanced applications, implement IVR capabilities to allow users to interact with the `afz1` system via voice commands over the phone.
*   **AI-Powered Voice Interactions:**  Incorporate AI models for more natural and intelligent voice interactions, such as using more advanced TTS engines or NLU for voice command processing.

## Code Location

*   `src/agents/phone_agent.py`

## Components

*   **BaseAgent (`src/agents/base_agent.py`):**  The `PhoneAgent` class inherits from `BaseAgent`, providing the basic agent lifecycle methods and configuration loading.

## Next Steps for Development

*   **Choose Telephony Service API:** Select a telephony service API (e.g., Twilio) for integration.
*   **Implement Outbound Call Initiation:** Implement the core logic to initiate outbound phone calls using the chosen telephony service API.
*   **Integrate Text-to-Speech (TTS):**  Incorporate a TTS engine to generate voice notifications from text alerts.
*   **(Optional) Implement Inbound Call Handling:**  Develop basic logic for handling inbound phone calls.
*   **User Interface for Phone Configuration:**  Create basic configuration settings for phone numbers and telephony service credentials.