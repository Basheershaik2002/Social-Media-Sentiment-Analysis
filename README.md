# Social-Media-Sentiment-Analysis

### Overview

Social Media Sentiment Analysis is a real-time interactive dashboard built using Streamlit.
It allows you to analyze social media posts (e.g., Twitter, Facebook, Instagram, YouTube) and understand public sentiment towards specific topics, products, or events.

The app uses Natural Language Processing (NLP) techniques to preprocess text data, extract sentiment scores, and visualize sentiment trends over time.

Live Demo: Click here to view (**https://social-media-sentiment-analysis-kuueyuaazdyjjy2s3bvmpz.streamlit.app/**)

### Features

- Real-time Sentiment Analyzer: Enter text (posts, reviews, comments) and get instant sentiment results.

- Multi-Platform Support: Analyze and filter posts by platform (Twitter, Facebook, Instagram, YouTube).

- Dashboard Metrics: View total posts, Positive %, Negative %, and Neutral %.

- Visualizations:

Bar chart & Pie chart for sentiment distribution

Word cloud for trending keywords

- Filters: Search by keyword, platform, and date range.

How to Run Locally

1️.Clone the repo
git clone https://github.com/<your-username>/sentiment-analysis-tool.git
cd sentiment-analysis-tool

2.Create a virtual environment
python -m venv venv
#### Activate (Windows)
venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run analysis.py


The app will open in your browser at http://localhost:8501.

### Tech Stack

Python 3.10+

Streamlit → Interactive web dashboard

TextBlob → Sentiment analysis (NLP)

Pandas → Data manipulation & filtering

Matplotlib → Charts & graphs

WordCloud → Trending keyword visualization

##### This project showcases my ability to design, develop, and deploy interactive data applications that provide real-time insights into social media sentiment
