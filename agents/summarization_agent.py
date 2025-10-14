# agents/summarization_agent.py

from transformers import pipeline

# Initialize Hugging Face summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    """
    Summarizes input text using Hugging Face local model.
    """
    # Hugging Face models have a max token limit, so split if necessary
    max_chunk = 500
    if len(text) > max_chunk:
        text = text[:max_chunk]  # take first 500 characters for simplicity

    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']

if __name__ == "__main__":
    # Test example
    sample_text = "Stocks rise. Market positive sentiment. Tech leading the rally today in Nasdaq. Investors optimistic."
    summary = summarize_text(sample_text)
    print("Summary:", summary)
