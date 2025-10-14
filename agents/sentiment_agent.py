from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

finbert = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiment(news_list):
    return [(title, finbert(title)[0]) for title, desc in news_list]

if __name__ == "__main__":
    sample_news = [("Stocks soar today", ""), ("Market crashes", "")]
    results = analyze_sentiment(sample_news)
    print(results)
