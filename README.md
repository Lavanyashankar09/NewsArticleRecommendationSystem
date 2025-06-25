

<img width="300" alt="image" src="https://github.com/user-attachments/assets/d0d99f47-c412-4fc6-be84-f3e987f083ee" />


# News Article Recommendation System

---

## Old Version — Streamlit + Heroku

**Built with:** Python, NumPy, Pandas, Seaborn, Matplotlib, Plotly, NLTK, scikit-learn, Pickle, Streamlit
**Tools:** Jupyter Notebook, Spyder, Docker, Heroku
**Website:** [news-article-recommender.herokuapp.com](http://news-article-recommender.herokuapp.com/)

**Goal:** Recommend articles that best fit user preferences.

### Highlights:

1. Developed a web scraper using Cypress to retrieve story details from *The New Yorker* website.
2. Fetches 90 news articles daily and appends new articles every other day.
3. Automated web scraping with a CI/CD pipeline.
4. Made pipeline OS-independent using Cypress Docker containerization.
5. Employed TF-IDF and Word2Vec embeddings for article recommendations.
6. Found Word2Vec performed better in capturing semantic similarity.
7. Deployed the application on Heroku and Docker for ease of access.

---

## New Version — FastAPI + HTML + Google Cloud Run

A modern web application that recommends news articles based on a headline input using FastAPI and TF-IDF similarity, with a clean HTML/CSS/JavaScript frontend.

---

### Features

* Enter a news headline and get real-time article recommendations.
* Backend powered by **FastAPI** with efficient similarity computations using **scikit-learn**.
* Minimalistic frontend using plain **HTML**, **CSS**, and JavaScript for a responsive user experience.
* Fully containerized with **Docker** for portability and ease of deployment.
* Easily deployable locally or on cloud platforms like **Google Cloud Run**.

---

### Project Structure

```
├── Backend/           # FastAPI backend API code
├── Frontend/          # HTML, CSS, and JavaScript frontend files
├── Pickle/            # Serialized data and TF-IDF model pickle files
├── Dockerfile         # Docker configuration for containerizing the app
├── README.md          # Project documentation (this file)
└── requirements.txt   # Python dependencies (optional)
```

---

### Getting Started

#### Prerequisites

* Python 3.7 or higher
* Docker (for containerized deployment)
* (Optional) Google Cloud SDK for deployment to Cloud Run

---

#### Run Locally Without Docker

1. Install required Python packages:

   ```bash
   pip install fastapi uvicorn scikit-learn pandas numpy python-multipart
   ```

2. Start the FastAPI backend server:

   ```bash
   uvicorn Backend.app:app --reload --port 8080
   ```

3. Open `Frontend/index.html` in your browser to access the UI.

---

#### Run With Docker

1. Build the Docker image:

   ```bash
   docker build -t news-recommendation-app .
   ```

2. Run the container locally:

   ```bash
   docker run -p 8080:8080 news-recommendation-app
   ```

3. Open [http://localhost:8080](http://localhost:8080) in your browser.

---

#### Deploy on Google Cloud Run

1. Configure your GCP project and build the Docker image:

   ```bash
   gcloud config set project YOUR_PROJECT_ID
   docker build -t gcr.io/YOUR_PROJECT_ID/news-recommendation-app .
   docker push gcr.io/YOUR_PROJECT_ID/news-recommendation-app
   ```

2. Deploy the container to Cloud Run:

   ```bash
   gcloud run deploy news-recommendation-app \
       --image gcr.io/YOUR_PROJECT_ID/news-recommendation-app \
       --platform managed \
       --region YOUR_REGION \
       --allow-unauthenticated \
       --port 8080
   ```

3. Access your deployed app via the URL provided by Cloud Run.

---

### Usage

* Start typing or select a headline from the suggestions.
* Click **Get Recommendations**.
* View a curated list of similar articles instantly below the input.

---

### Tech Stack

* **FastAPI** — Fast and modern web API framework
* **scikit-learn / nltk** — TF-IDF vectorization and cosine similarity calculations
* **HTML / CSS / JavaScript** — Frontend user interface
* **Docker** — Containerization for consistent environments
* **Google Cloud Run** — Serverless container hosting (optional cloud deployment)

---
