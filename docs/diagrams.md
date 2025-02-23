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

<!-- Add more diagrams below as needed -->