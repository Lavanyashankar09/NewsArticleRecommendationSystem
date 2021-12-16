# news_article_recommender

Built with  Python and Streamlit
Tools : Jupyter Notebook, Docker, Heroku

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
