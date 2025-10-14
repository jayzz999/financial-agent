import pandas as pd
from agents.summarization_agent import summarize_text

def generate_report(sentiment_results):
    df = pd.DataFrame([(t, r['label'], r['score']) for t, r in sentiment_results],
                      columns=["title", "sentiment", "confidence"])
    summary = summarize_text(" ".join(df['title'].tolist()))
    report = {
        "summary": summary,
        "positive": df[df['sentiment']=='positive'].shape[0],
        "negative": df[df['sentiment']=='negative'].shape[0],
        "neutral": df[df['sentiment']=='neutral'].shape[0]
    }
    return report
