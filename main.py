import streamlit as st
from collections import Counter
from agents.data_agent import fetch_news
from agents.sentiment_agent import analyze_sentiment
from agents.report_agent import generate_report
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Financial Market Summary", page_icon="📈")

st.title("Daily Financial Market Summary")
st.write("Real-time market sentiment analysis powered by FinBERT")

# Use session state to store results
if 'report' not in st.session_state:
    st.session_state.report = None
    st.session_state.news = None

# Button to trigger analysis
if st.button("🔄 Fetch & Analyze Latest News", type="primary"):
    with st.spinner("Fetching news articles..."):
        news = fetch_news()
        st.session_state.news = news
        st.success(f"✅ Fetched {len(news)} articles")
    
    with st.spinner("Analyzing sentiment with FinBERT..."):
        sentiments = analyze_sentiment(news)
        st.success("✅ Sentiment analysis complete")
    
    with st.spinner("Generating report..."):
        report = generate_report(sentiments)
        st.session_state.report = report
        st.success("✅ Report generated")

# Display results if they exist
if st.session_state.report:
    report = st.session_state.report
    news = st.session_state.news
    
    st.subheader("📊 Market Summary")
    st.write(report["summary"])
    
    st.subheader("📈 Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#28a745', '#6c757d', '#dc3545']
    bars = ax.bar(
        ["Positive", "Neutral", "Negative"],
        [report["positive"], report["neutral"], report["negative"]],
        color=colors
    )
    ax.set_ylabel('Number of Articles')
    ax.set_title('Market Sentiment Analysis')
    st.pyplot(fig)
    
    st.subheader("📰 Latest Headlines")
    for i, (title, _) in enumerate(news[:10], 1):
        st.write(f"{i}. {title}")
else:
    st.info("👆 Click the button above to start analyzing market sentiment")
