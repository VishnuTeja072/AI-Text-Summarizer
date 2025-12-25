from transformers import pipeline

# Lazy load summarization pipeline
summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )
    return summarizer

def summarize_text(text, max_length=150, min_length=50):
    if len(text.strip()) == 0:
        return "No text provided."

    # Truncate text to max 1024 tokens (~4096 characters)
    # BART model has a max input length of 1024 tokens
    max_chars = 1024 * 4
    text = text[:max_chars]

    summarizer_pipeline = get_summarizer()
    
    try:
        summary = summarizer_pipeline(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return summary[0]["summary_text"]
    except IndexError:
        return "Error: Text is too short or invalid for summarization. Please provide more content."
