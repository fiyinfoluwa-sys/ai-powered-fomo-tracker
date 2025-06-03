# 🔍 AI-Powered FOMO Tracker

**Independent Project | In Progress | 2025**

The **AI-Powered FOMO (Fear of Missing Out) Tracker** is a Python-based application designed to analyze, score, and visualize **trending social content** in real-time across platforms like **Reddit**, **X (formerly Twitter)**, and **Google Trends**. It leverages **NLP, sentiment analysis**, and **user-personalized filtering** to surface events, topics, and opportunities that align with user-defined interests or industries—helping users reduce the fear of missing out on relevant conversations or trends.

---

## 🧠 Key Objectives

- **Aggregate** real-time data from social platforms using public APIs.
- **Analyze** content using AI/ML models for sentiment, trend strength, and topic classification.
- **Score** trends based on relevance, virality, and user-defined priority.
- **Visualize** data via an interactive dashboard for insights and alerts.

---

## 🧰 Tech Stack & Tools

| Technology             | Purpose                                                   |
|------------------------|------------------------------------------------------------|
| **Python 3.11**         | Core application logic and data pipelines                 |
| **Reddit API (PRAW)**   | Data ingestion from subreddits of interest                |
| **Google Trends API (pytrends)** | Web search volume tracking                     |
| **OpenAI API**          | Natural language processing and summarization             |
| **Pandas / NumPy**      | Data processing and manipulation                          |
| **scikit-learn**        | Trend scoring and basic machine learning classification   |
| **Matplotlib / Plotly** | Trend visualization & interactive graphs                  |
| **Streamlit**           | Lightweight web dashboard frontend                        |

---

## ⚙️ Features

### ✅ Current Capabilities

- 🔄 Real-time scraping of Reddit subreddit activity
- 💬 NLP-based keyword extraction and topic modeling (via OpenAI GPT)
- 📈 Trend scoring using frequency, velocity, and sentiment metrics
- 📊 Streamlit-based trend dashboard with auto-refresh intervals
- 📌 Local keyword/watchlist matching for FOMO-relevance scoring

### 🚀 Future Features

- 📣 Alert system for spikes in topic relevance (SMS/Email via Twilio)
- 🔍 Integration with X (Twitter) API and YouTube Trending Feed
- 👤 User profiles and customizable interest vectors
- 📂 Caching via SQLite or Firebase for faster load and historical views
- 📤 Export options for trend reports (PDF, CSV, or Notion integration)

---

## 🧠 Sample Use Case

**Scenario:** A startup founder interested in AI, climate tech, and funding rounds sets a personalized watchlist.

1. The FOMO Tracker scrapes posts from `/r/startups`, `/r/MachineLearning`, and Google Trends.
2. A post titled *“OpenAI launches GPT-6 for enterprise users”* spikes in activity.
3. NLP analysis evaluates sentiment, keyword match, and velocity.
4. A high FOMO-score is calculated (based on relevance + trending rate).
5. The system flags the post, adds it to the user’s dashboard feed, and optionally sends a push notification or email.
6. The founder clicks through to view the full post and shares it with their network—ensuring they stay informed in real-time.

