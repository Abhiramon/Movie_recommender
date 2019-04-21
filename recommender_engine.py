
# coding: utf-8

# # Movies Recommender System

# <img src='http://labs.criteo.com/wp-content/uploads/2017/08/CustomersWhoBought3.jpg', width=500>

# This is the second part of my Springboard Capstone Project on Movie Data Analysis and Recommendation Systems. In my first notebook, I attempted at narrating the story of film by performing an extensive exploratory data analysis on Movies Metadata collected from TMDB. I also built two extremely minimalist predictive models to predict movie revenue and movie success and visualise which features influence the output (revenue and success respectively).
#
# In this notebook, I will attempt at implementing a few recommendation algorithms (content based, popularity based and collaborative filtering) and try to build an ensemble of these models to come up with our final recommendation system. With us, we have two MovieLens datasets.
#
# * **The Full Dataset:** Consists of 26,000,000 ratings and 750,000 tag applications applied to 45,000 movies by 270,000 users. Includes tag genome data with 12 million relevance scores across 1,100 tags.
# * **The Small Dataset:** Comprises of 100,000 ratings and 1,300 tag applications applied to 9,000 movies by 700 users.
#
# We will build our Simple Recommender using movies from the *Full Dataset* whereas all personalised recommender systems will make use of the small dataset (due to the computing power I possess being very limited). As a first step, let us build our simple recommender system.

# In[24]:

import time
import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

# from surprise import Reader, Dataset, SVD, evaluate

import warnings; warnings.simplefilter('ignore')


# In[25]:

def get_recommendations(title, number_of_recommendations):

    smd = pd.read_csv('data/smd.txt')


    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smd['description'].values.astype('U'))

    # In[33]:


    # In[34]:


    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # In[35]:

    # We now have a pairwise cosine similarity matrix for all the movies in our dataset. The next step is to write a function that returns the 30 most similar movies based on the cosine similarity score.

    # In[36]:


    smd = smd.reset_index()
    titles = smd['title']
    indices = pd.Series(smd.index, index=smd['title'])


    # In[37]:



    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    #Select from 1 to exclude the title
    sim_scores = sim_scores[1:number_of_recommendations + 1]

    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]



# In[38]:

# print(get_recommendations('The Godfather', 5)
#
#
# # In[39]:
#
#
# get_recommendations('The Dark Knight', 5)
