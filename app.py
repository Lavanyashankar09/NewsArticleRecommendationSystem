import pickle
import streamlit as st
import numpy as np
from sklearn.metrics import pairwise_distances

st.title("news article recommendation system")

def recommend(new):
    recommend_news = [] 
    row_index = news_articles[news_articles['headline'] == new].index[0]
    couple_dist = pairwise_distances(tfidf_headline_features,tfidf_headline_features[row_index])
    indices = np.argsort(couple_dist.ravel())[0:8]
    recommend_news.append(news_articles['headline'][indices])
    return (recommend_news)
    
news_articles = pickle.load(open('news_articles_list.pkl','rb'))
tfidf_headline_features = pickle.load(open('similarity.pkl','rb'))


news_articles_list = news_articles['headline'].values
selected_news_articles = st.selectbox(
    "Type or select a news article from the dropdown",
    news_articles_list
)

if st.button('Show Recommendation'):
    recommend_news = recommend(selected_news_articles)
    st.text(recommend_news)
    
        