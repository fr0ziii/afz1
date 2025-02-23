# Project Diagrams

This file contains diagrams of the project architecture, agent communication patterns, and other relevant system designs, using Mermaid syntax.

## Architecture Diagram

```mermaid
graph LR
    A[Agent Manager] --> B(Agent 1)
    A --> C(Agent 2)
    A --> D(Agent 3)
    B --> MQ[Message Queue]
    C --> MQ
    D --> MQ
    MQ --> E{Data Storage}
    MQ --> F[External APIs]
```

## Agent Communication Diagram

```mermaid
sequenceDiagram
    participant Agent1
    participant Message Queue
    participant Agent2

    Agent1->>Message Queue: Publish Message
    Message Queue-->>Agent2: Deliver Message
    Agent2->>Message Queue: Request Data
    Message Queue-->>Agent1: Respond with Data
```

## Component Diagram

```mermaid
graph LR
    subgraph Core System
        AgentManager[Agent Manager]
        MessageQueue[Message Queue]
        DataStorage[Data Storage]
    end

    subgraph Agents
        ChartAnalysisAgent
        TradingAgent
        SentimentAgent
        RiskAgent
        ...
    end

    subgraph Data
        MarketDataProviders[Market Data Providers]
        ExternalAPIs[External APIs]
    end

    subgraph Strategies
        BaseStrategy[Base Strategy]
        CustomStrategies[...]
    end

    subgraph Models
        AIModels[AI Models]
        ModelFactory[Model Factory]
    end

    subgraph Web Interface
        Frontend[Frontend UI]
        ChatInterface[Chat Interface]
    end

    AgentManager --> Agents
    AgentManager --> MessageQueue
    Agents --> MessageQueue
    MessageQueue --> DataStorage
    MessageQueue --> MarketDataProviders
    MarketDataProviders --> ExternalAPIs
    Agents --> Strategies
    Agents --> Models
    Frontend --> AgentManager
    ChatInterface --> AgentManager
    ModelFactory --> AIModels
    Strategies --> BaseStrategy
    DataStorage --> Data
    ExternalAPIs --> Data
```

## Deployment Diagram

```mermaid
graph LR
    User[User] -- Uses --> LocalMachine[Local Machine]
    LocalMachine -- Runs --> System[afz1 System]
    System -- Accesses Data from --> ExternalAPIs[External APIs (e.g., Binance, Etherscan)]

    subgraph Cloud Deployment
        CloudServer[Cloud Server] -- Runs --> CloudSystem[afz1 System (Cloud)]
        CloudSystem -- Accesses Data from --> ExternalAPIs
        User -- Accesses --> CloudSystem
    end

    LocalMachine -- Optionally Deploys to --> CloudServer
```

## Data Flow Diagram

```mermaid
graph LR
    ExternalDataSources[External Data Sources (e.g., Binance API, Etherscan API)] --> MarketDataProviders[Market Data Providers]
    MarketDataProviders --> MessageQueue[Message Queue]
    MessageQueue --> Agents[Trading Agents]
    Agents --> SignalGenerator[Signal Generator]
    SignalGenerator --> OrderExecution[Order Execution Module]
    OrderExecution --> ExchangeAPI[Exchange API]
    Agents --> DataStorage[Data Storage]
    DataStorage --> UserInterface[User Interface (Web/CLI)]
    Agents --> UserInterface
    UserInterface -- Receives Feedback from --> User

    style MessageQueue fill:#f9f,stroke:#333,stroke-width:2px
    style Agents fill:#ccf,stroke:#333,stroke-width:2px
    style DataStorage fill:#cfc,stroke:#333,stroke-width:2px
    style UserInterface fill:#fcc,stroke:#333,stroke-width:2px
```

<!-- Add more diagrams below as needed -->