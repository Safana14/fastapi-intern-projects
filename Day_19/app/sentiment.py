from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):
    result = classifier(text)[0]

    return {
        "sentiment": result["label"],
        "score": float(result["score"])
    }