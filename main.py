import streamlit as st
from collections import Counter

from agents.data_agent import fetch_news
from agents.sentiment_agent import analyze_sentiment
from agents.report_agent import generate_report

import matplotlib.pyplot as plt

news = fetch_news()
sentiments = analyze_sentiment(news)
report = generate_report(sentiments)

st.title("Daily Financial Market Summary")
st.write(report["summary"])

fig, ax = plt.subplots()
ax.bar(["Positive", "Neutral", "Negative"],
[report["positive"], report["neutral"], report["negative"]])
st.pyplot(fig)

st.write("Latest News:")
for t, _ in news[:10]:
    st.write("-", t)