# news_article_recommender

Built with python, NumPy, pandas, seaborn, matplotlib, ploty, nltk, sklearn, pickle, streamlit.

Tools: Jupyter Notebook, Spyder, Docker, Heroku.

website - http://news-article-recommender.herokuapp.com/

AIM - recommend articles that best fit the user’s preferences

Steps:
1. created a web scraper with cypress to retrieve the story's details from the New Yorker website. 
2. Per day the program fetches 90 news articles and every other day it just appends the articles.
3. I automated web scraping by building a CI/CD pipeline.
4. I made this pipeline OS independent by using the cypress docker approach
5. Employed the TF-IDF technique and Word2Vec word embeddings to recommned articles
6. Word2Vec, the unsupervised model, did well in comparison.
7. Deployed the app on Heroku and Docker


# Part 2 - News Article Recommendation System (FastAPI+HTML)

A web application that recommends news articles based on a headline input using FastAPI, TF-IDF vector similarity, and a simple HTML frontend.

---

## Features

* Input a news headline and get similar article recommendations.
* Backend powered by **FastAPI** with similarity calculations using **scikit-learn**.
* Frontend built with plain **HTML**, **CSS**, and JavaScript for a smooth user experience.
* Containerized with **Docker** for easy deployment.
* Can be deployed locally or on cloud platforms like **Google Cloud Run**.

---

## Project Structure

```
├── Backend/           # FastAPI backend code
├── Frontend/          # HTML, CSS, JavaScript files
├── Pickle/            # Preprocessed data and TF-IDF features saved as pickle files
├── Dockerfile         # Docker configuration for containerizing the app
├── README.md          # This documentation
└── requirements.txt   # Python dependencies (optional)
```

---

## Getting Started

### Prerequisites

* Python 3.7+
* Docker (for containerized setup)
* (Optional) Google Cloud SDK for deployment

---

### Run Locally without Docker

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn scikit-learn pandas numpy python-multipart
   ```

2. Start the FastAPI backend:

   ```bash
   uvicorn Backend.app:app --reload --port 8080
   ```

3. Open `Frontend/index.html` in your browser to use the app.

---

### Run with Docker

1. Build Docker image:

   ```bash
   docker build -t news-recommendation-app .
   ```

2. Run Docker container:

   ```bash
   docker run -p 8080:8080 news-recommendation-app
   ```

3. Access app at: [http://localhost:8080](http://localhost:8080)

---

### Deploy on Google Cloud Run

1. Configure your GCP project and build image:

   ```bash
   gcloud config set project YOUR_PROJECT_ID
   docker build -t gcr.io/YOUR_PROJECT_ID/news-recommendation-app .
   docker push gcr.io/YOUR_PROJECT_ID/news-recommendation-app
   ```

2. Deploy to Cloud Run:

   ```bash
   gcloud run deploy news-recommendation-app \
       --image gcr.io/YOUR_PROJECT_ID/news-recommendation-app \
       --platform managed \
       --region YOUR_REGION \
       --allow-unauthenticated \
       --port 8080
   ```

3. Open the URL provided by Cloud Run.

---

## Usage

* Enter or select a headline in the input box.
* Click **Get Recommendations**.
* View recommended similar articles below.

---

## Tech Stack

* **FastAPI** — Backend API framework
* **scikit-learn** — TF-IDF vectorization and similarity calculations
* **HTML/CSS/JavaScript** — Frontend UI
* **Docker** — Containerization
* **Google Cloud Run** (optional) — Cloud deployment

---
