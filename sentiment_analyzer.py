from textblob import TextBlob

def analyze_sentiment(text: str):
    """
    Analyze sentiment using TextBlob.
    Returns sentiment label and polarity score.
    """
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive", polarity
    elif polarity < 0:
        return "Negative", polarity
    else:
        return "Neutral", polarity
