import asyncio
from functools import lru_cache
from transformers import pipeline

@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

def _run_sentiment_sync(text: str) -> dict:
    classifier = get_sentiment_pipeline()
    result = classifier(text)[0]
    return {"label": result["label"], "score": round(float(result["score"]), 4)}

async def analyze_sentiment(text: str) -> dict:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _run_sentiment_sync, text)