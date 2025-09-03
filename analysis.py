import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
import random
from datetime import datetime, timedelta

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Social Media Sentiment Analysis", layout="wide")

st.title("📊 Social Media Sentiment Analysis Tool")
st.write("Analyze social media data (e.g., Twitter, Facebook, Instagram, YouTube) to understand public sentiment towards topics, products, or events.")

# -------------------------------
# Initialize Session State Dataset
# -------------------------------
if "df" not in st.session_state:
    platforms = ["Twitter", "Facebook", "Instagram", "YouTube"]
    today = datetime.today()

    data = {
        "post": [
            "I love this product!", "Terrible delivery service", "Amazing experience",
            "The app is buggy", "Customer support was helpful", "I hate the new update",
            "The design is beautiful", "Battery life is disappointing", "Camera is incredible",
            "Overall okay but slow"
        ]
    }

    df = pd.DataFrame(data)
    df["platform"] = [random.choice(platforms) for _ in range(len(df))]
    df["date"] = [today - timedelta(days=random.randint(0, 30)) for _ in range(len(df))]
    df["polarity"] = df["post"].apply(lambda x: TextBlob(x).sentiment.polarity)
    df["sentiment"] = df["polarity"].apply(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral"))

    st.session_state.df = df

# Always work with session dataset
df = st.session_state.df

# -------------------------------
# Real-time Sentiment Analyzer
# -------------------------------
st.header("📝 Real-time Sentiment Analyzer")

col_input, col_platform = st.columns([3, 1])

with col_input:
    user_input = st.text_area(
        "Enter text to analyze sentiment... (e.g., social media posts, reviews, comments)",
        height=100
    )

with col_platform:
    selected_input_platform = st.selectbox("Platform", ["Twitter", "Facebook", "Instagram", "YouTube"])

if user_input.strip():
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"
        sentiment_label = "Positive"
        color = "green"
    elif polarity < 0:
        sentiment = "Negative 😡"
        sentiment_label = "Negative"
        color = "red"
    else:
        sentiment = "Neutral 😐"
        sentiment_label = "Neutral"
        color = "gray"

    st.markdown(
        f"<div style='background-color:#f0f0f0;padding:10px;border-radius:8px'>"
        f"<b>Sentiment:</b> <span style='color:{color};font-weight:bold'>{sentiment}</span><br>"
        f"<b>Polarity Score:</b> {polarity:.2f}</div>",
        unsafe_allow_html=True
    )

    # Save new row permanently in session_state
    new_row = pd.DataFrame([{
        "post": user_input,
        "platform": selected_input_platform,
        "date": datetime.today(),
        "polarity": polarity,
        "sentiment": sentiment_label
    }])

    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    df = st.session_state.df

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔎 Filters")

platforms_filter = ["All platforms", "Twitter", "Facebook", "Instagram", "YouTube"]
selected_platform = st.sidebar.selectbox("Platform", platforms_filter)

keyword = st.sidebar.text_input("Search Keywords (e.g., #AI, product, delivery)")
date_range = st.sidebar.date_input("Select Date Range", [])

filtered_df = df.copy()

if selected_platform != "All platforms":
    filtered_df = filtered_df[filtered_df["platform"] == selected_platform]

if keyword:
    filtered_df = filtered_df[filtered_df["post"].str.contains(keyword, case=False, na=False)]

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[(filtered_df["date"] >= pd.to_datetime(start_date)) &
                              (filtered_df["date"] <= pd.to_datetime(end_date))]

st.sidebar.success(f"{len(filtered_df)} posts found after filtering")

# -------------------------------
# Overall Metrics
# -------------------------------
st.header("📊 Overall Metrics")
col1, col2, col3, col4 = st.columns(4)

total_posts = len(filtered_df)
positive_count = sum(filtered_df["sentiment"] == "Positive")
negative_count = sum(filtered_df["sentiment"] == "Negative")
neutral_count = sum(filtered_df["sentiment"] == "Neutral")

col1.metric("Total Posts", total_posts)
col2.metric("Positive %", f"{(positive_count/total_posts)*100:.1f}%" if total_posts > 0 else "0%")
col3.metric("Negative %", f"{(negative_count/total_posts)*100:.1f}%" if total_posts > 0 else "0%")
col4.metric("Neutral %", f"{(neutral_count/total_posts)*100:.1f}%" if total_posts > 0 else "0%")

# -------------------------------
# Charts & Word Cloud
# -------------------------------
if total_posts > 0:
    st.header("📈 Sentiment Distribution")
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        filtered_df["sentiment"].value_counts().plot(kind="bar", color=["green", "red", "gray"], ax=ax)
        plt.title("Sentiment Count")
        st.pyplot(fig)

    with col6:
        st.subheader("Pie Chart")
        fig, ax = plt.subplots()
        filtered_df["sentiment"].value_counts().plot.pie(
            autopct="%1.1f%%", colors=["green", "red", "gray"], ax=ax, startangle=90
        )
        plt.ylabel("")
        plt.title("Sentiment Share")
        st.pyplot(fig)

    st.header("☁️ Trending Keywords")
    all_text = " ".join(filtered_df["post"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("⚠️ No posts match your filters.")
