from fastapi import FastAPI, Query, Body
from typing import Optional
from textblob import TextBlob

from fastapi.middleware.cors import CORSMiddleware

import traceback

app = FastAPI()
PERPLEXITY_API_KEY='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'

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],           
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root():
    return {"message": "Hello, FastAPI!"}

def analyze_sentiment(review: str):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.post("/post-review")
async def post_review(review: str = Body(..., embed=True)):
    try:
        result = analyze_sentiment(review)
        return {"result": result}

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
    

