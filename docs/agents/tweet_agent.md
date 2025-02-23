# Tweet Agent

## Description

The Tweet Agent is designed for monitoring and analyzing Twitter/X data and trends. It provides a basic framework for agents that can track tweets, analyze tweet sentiment, identify trending topics, and potentially generate signals based on Twitter/X data analysis. This agent can be valuable for traders and analysts who want to incorporate social media sentiment and trends from Twitter/X into their market analysis or trading strategies.

## Missions

[Description of the missions this agent is designed to accomplish. Link to mission files if applicable.]
- **Real-time sentiment monitoring of specific cryptocurrencies:** Continuously track the overall sentiment towards Bitcoin, Ethereum, and other major cryptocurrencies on Twitter/X.
- **Detection of trending crypto-related topics:** Identify emerging hashtags and topics related to cryptocurrencies that are gaining traction on Twitter/X.
- **Alerting on significant sentiment shifts:** Trigger alerts when there are sudden or significant changes in the sentiment towards specific cryptocurrencies, potentially indicating market-moving events.
- **Analyzing tweet sentiment during periods of high market volatility:** Examine how Twitter/X sentiment changes during periods of high price volatility in cryptocurrency markets.
- **Correlating tweet sentiment with price movements:** Investigate the correlation between Twitter/X sentiment and cryptocurrency price changes to assess the predictive power of social media sentiment.
- Currently, no specific mission files are defined for the Tweet Agent, but missions can be further specified based on the above points.

## Configuration

The Tweet Agent requires the following configuration parameters, in addition to the basic parameters inherited from `BaseAgent`:

-   **agent_id**: A unique identifier for the agent instance.
-   **agent_type**: Must be set to `TweetAgent`.
-   **twitter_api_key**: (Required) API key for accessing the Twitter/X API.
-   **twitter_api_secret**: (Required) API secret for accessing the Twitter/X API.
-   **monitored_keywords**: (Optional) A list of keywords or hashtags to monitor on Twitter/X (e.g., `["bitcoin", "#ethereum"]`).
-   **language**: (Optional) Language for filtering tweets (e.g., `"en"` for English).
-   **sentiment_analysis_model**: (Optional) Specify the sentiment analysis model to use (e.g., `"vader"`, `"textblob"`).
-   **alert_threshold**: (Optional) Sentiment score threshold to trigger alerts (e.g., `-0.7` for strong negative sentiment).

### Example Configuration

```yaml
config:
  agent_id: tweet_agent_01
  agent_type: TweetAgent
  # Add any tweet monitoring specific configurations here in the future
  # e.g., twitter_api_key, twitter_api_secret, monitored_keywords, analysis_parameters
  twitter_api_key: "YOUR_API_KEY"
  twitter_api_secret: "YOUR_API_SECRET"
  monitored_keywords: ["bitcoin", "#eth", "cryptocurrency"]
  language: "en"
  sentiment_analysis_model: "vader"
  alert_threshold: -0.6
```

## Inputs and Outputs

### Inputs

-   **Twitter/X API**: 
    - Real-time tweet stream from the Twitter/X API.
    - Historical tweet data (if implemented in future versions).
    - Data is filtered based on:
      - **Monitored Keywords**: User-defined keywords and hashtags to track relevant tweets.
      - **Language Filter**: (Optional) Filter tweets by language (e.g., English).
-   **Configuration Parameters**: 
    - Agent configuration settings loaded at startup, including API keys, monitored keywords, and analysis parameters.

### Outputs

-   **Tweet Sentiment Scores**: 
    - Numerical sentiment scores assigned to individual tweets or aggregated sets of tweets.
    - Sentiment polarity (positive, negative, neutral) and intensity.
    - Scores can be generated using different sentiment analysis models (e.g., VADER, TextBlob).
-   **Trending Topics and Hashtags**: 
    - List of trending topics and hashtags related to cryptocurrencies identified from the monitored tweet stream.
    - Trend intensity or ranking (if applicable).
-   **Sentiment Shift Alerts**: 
    - Real-time alerts triggered when significant shifts in market sentiment are detected.
    - Alert triggers can be based on:
      - **Sentiment Score Thresholds**: Crossing predefined sentiment score levels (e.g., extreme positive or negative sentiment).
      - **Sentiment Change Rate**: Rapid changes in sentiment scores over a short period.
-   **Raw Tweet Data (Optional, for logging/debugging)**: 
    - Raw tweet data can be logged for detailed analysis, debugging, or auditing purposes.
-   **Logs**: Informational and error logs for monitoring agent activity and debugging.

## Workflow

The Tweet Agent operates through the following workflow:

1.  **Initialization and Configuration**:
    - On startup, the agent loads configuration parameters, including Twitter/X API credentials, monitored keywords, and sentiment analysis settings.
2.  **Connect to Twitter/X API**:
    - The agent establishes a connection to the Twitter/X API using the provided API keys and secrets.
    - Handles API authentication and connection setup.
3.  **Real-time Tweet Stream Monitoring**:
    - The agent initiates a real-time stream of tweets from the Twitter/X API.
    - The stream is filtered based on the configured `monitored_keywords` and `language` (if specified).
4.  **Tweet Data Processing**:
    - As tweets are received from the stream, the agent processes each tweet individually or in batches.
    - Preprocessing steps may include text cleaning, stop word removal, and tokenization.
5.  **Sentiment Analysis**:
    - The agent performs sentiment analysis on the tweet text content using the specified `sentiment_analysis_model` (e.g., VADER, TextBlob).
    - Assigns sentiment scores (polarity and intensity) to each tweet.
6.  **Trending Topic Detection**:
    - The agent analyzes the tweet stream to identify trending topics and hashtags related to cryptocurrencies.
    - Trend detection algorithms may be used to identify emerging and popular topics.
7.  **Sentiment Shift and Trend Alerting**:
    - The agent monitors aggregated sentiment scores and trending topics for significant changes or patterns.
    - Generates real-time alerts based on predefined thresholds or conditions:
      - **Sentiment Alerts**: Triggered by extreme sentiment scores or rapid sentiment shifts.
      - **Trending Topic Alerts**: Triggered by the emergence of significant new topics or hashtags.
8.  **Output and Reporting**:
    - The agent outputs sentiment scores, trending topics, and generated alerts.
    - (Future) May include more detailed reports and visualizations of sentiment analysis and trend data.
9.  **Logging and Monitoring**:
    - The agent logs all activities, including API interactions, data processing, sentiment analysis results, identified trends, and generated alerts.
    - Logs are used for monitoring agent performance, debugging, and auditing purposes.
10. **Continuous Monitoring**:
    - The agent continuously monitors the tweet stream and repeats steps 3-9 in real-time to provide ongoing sentiment and trend analysis.

## Example Usage

To run the Tweet Agent, you would instantiate it with a configuration including Twitter/X API credentials and monitoring parameters. Below is an example of how to configure and run the `TweetAgent` (note that API keys are placeholders and should be replaced with your actual API keys):

```python
from src.agents.tweet_agent import TweetAgent

config = {
    "agent_id": "tweet_agent_01",
    "agent_type": "TweetAgent",
    "twitter_api_key": "YOUR_TWITTER_API_KEY",  # Replace with your actual API key
    "twitter_api_secret": "YOUR_TWITTER_API_SECRET", # Replace with your actual API secret
    "monitored_keywords": ["bitcoin", "#eth", "crypto"],
    "language": "en",
    "sentiment_analysis_model": "vader",
    "alert_threshold": -0.7,
}

agent = TweetAgent(config)
# agent.run() # In future implementations, run method would start tweet monitoring

# In a future version, you might have methods to start and stop tweet monitoring explicitly:
# agent.start_tweet_monitoring()
# agent.stop_tweet_monitoring() 
```

In this example, the configuration includes:

-   `twitter_api_key` and `twitter_api_secret`: Placeholder API credentials that you need to replace with your actual Twitter/X API keys.
-   `monitored_keywords`: A list of keywords to track on Twitter/X (e.g., "bitcoin", "#eth", "crypto").
-   `language`:  Filters tweets to only include English tweets (`"en"`).
-   `sentiment_analysis_model`: Specifies the sentiment analysis model to be used (`"vader"` in this case).
-   `alert_threshold`: Sets the sentiment score threshold for triggering alerts (e.g., strong negative sentiment below `-0.7`).

After instantiating the agent with this configuration, you would typically call the `run()` method (or a similar method like `start_tweet_monitoring()` in future versions) to begin monitoring tweets and analyzing sentiment.

## Code Location

-   `src/agents/tweet_agent.py`

## Components

-   **BaseAgent (`src/agents/base_agent.py`):**  The Tweet Agent inherits basic agent functionalities from the `BaseAgent`.
-   **Twitter/X API Components (To be implemented)**: Future implementations would include components for connecting to the Twitter/X API and fetching tweet data using libraries like Tweepy or similar.
-   **Tweet Analysis Components (Future)**: Components for analyzing tweet data, including sentiment analysis, trend detection, and keyword extraction.
-   **Alerting Components (Future)**: Components for generating and delivering alerts based on tweet sentiment, trending topics, or specific tweet content.

## Notes and Considerations

-   **Placeholder Implementation**: The current `TweetAgent` is a basic placeholder. Significant implementation is required to add actual tweet monitoring and analysis capabilities.
-   **Twitter/X API Integration**:  Implementing Twitter/X API integration requires handling API authentication, rate limits, and data streaming for the Twitter/X API.
-   **Data Source Selection**:  Define relevant keywords, hashtags, and user accounts to monitor on Twitter/X for effective market sentiment analysis.
-   **Sentiment Analysis Techniques**:  Choose appropriate NLP techniques and sentiment analysis models for analyzing tweet text content and deriving meaningful sentiment scores.
-   **Real-time Data Processing**:  Implement real-time data processing pipelines to capture and analyze tweets in a timely manner for relevant market insights.
-   **API Rate Limits and Data Handling**: Be mindful of Twitter/X API rate limits and implement efficient data handling and storage mechanisms to manage large volumes of tweet data.