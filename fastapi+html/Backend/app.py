from fastapi import FastAPI, HTTPException, Query, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PICKLE_DIR = os.path.join(BASE_DIR, 'Pickle')
FRONTEND_DIR = os.path.join(BASE_DIR, 'Frontend')

news_articles = pickle.load(open(os.path.join(PICKLE_DIR, 'news_articles_list.pkl'), 'rb'))
tfidf_features = pickle.load(open(os.path.join(PICKLE_DIR, 'similarity.pkl'), 'rb'))

# Serve static files (if you have any CSS/JS/images in Frontend/static)
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR, "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Serve the raw index.html file from Frontend folder
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    return FileResponse(index_path)

@app.post("/recommend")
async def recommend(headline: str = Form(...)):
    if headline not in news_articles['headline'].values:
        return {"error": "Headline not found!"}

    row_index = news_articles[news_articles['headline'] == headline].index[0]
    distances = pairwise_distances(tfidf_features, tfidf_features[row_index])
    similar_indices = np.argsort(distances.ravel())[1:4]
    recommendations = news_articles['headline'].iloc[similar_indices].tolist()

    return {"input_headline": headline, "recommendations": recommendations}
