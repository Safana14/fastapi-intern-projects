from transformers import pipeline

_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            'sentiment-analysis',
            model='distilbert/distilbert-base-uncased-finetuned-sst-2-english'
        )
    return _classifier

def analyze_sentiment(text: str):
    classifier = get_classifier()
    result = classifier(text)[0]
    return {
        'sentiment': result['label'],
        'score': float(result['score'])
    }