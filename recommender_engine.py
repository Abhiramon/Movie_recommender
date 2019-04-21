
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
import matplotlib.pyplot as plt
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD, evaluate

import warnings; warnings.simplefilter('ignore')


# In[25]:

def get_recommendations(title):

    # md = pd. read_csv('data/movies_metadata.csv')
    #
    #
    # # In[26]:
    # #Measuring time for performance improvements
    # start = time.time()
    #
    # md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
    #
    # end = time.time()
    # print("md Creation: " + str(end - start))
    # # ## Content Based Recommender
    # #
    # # The recommender we built in the previous section suffers some severe limitations. For one, it gives the same recommendation to everyone, regardless of the user's personal taste. If a person who loves romantic movies (and hates action) were to look at our Top 15 Chart, s/he wouldn't probably like most of the movies. If s/he were to go one step further and look at our charts by genre, s/he wouldn't still be getting the best recommendations.
    # #
    # # For instance, consider a person who loves *Dilwale Dulhania Le Jayenge*, *My Name is Khan* and *Kabhi Khushi Kabhi Gham*. One inference we can obtain is that the person loves the actor Shahrukh Khan and the director Karan Johar. Even if s/he were to access the romance chart, s/he wouldn't find these as the top recommendations.
    # #
    # # To personalise our recommendations more, I am going to build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as **Content Based Filtering.**
    # #
    # # I will build two Content Based Recommenders based on:
    # # * Movie Overviews and Taglines
    # # * Movie Cast, Crew, Keywords and Genre
    # #
    # # Also, as mentioned in the introduction, I will be using a subset of all the movies available to us due to limiting computing power available to me.
    #
    # # In[27]:
    # #Measuring time for performance improvements
    # start = time.time()
    #
    # links_small = pd.read_csv('data/links_small.csv')
    # links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
    #
    # end = time.time()
    # print("links_small Creation: " + str(end - start))
    #
    #
    #
    #
    # # In[28]:
    #
    #
    # md = md.drop([19730, 29503, 35587])
    #
    #
    # # In[29]:
    #
    #
    # #Check EDA Notebook for how and why I got these indices.
    # md['id'] = md['id'].astype('int')
    #
    #
    # # In[30]:
    # #Measuring time for performance improvements
    # start = time.time()
    #
    #
    # smd = md[md['id'].isin(links_small)]
    #
    #
    # # We have **9099** movies avaiable in our small movies metadata dataset which is 5 times smaller than our original dataset of 45000 movies.
    #
    # # ### Movie Description Based Recommender
    # #
    # # Let us first try to build a recommender using movie descriptions and taglines. We do not have a quantitative metric to judge our machine's performance so this will have to be done qualitatively.
    #
    # # In[31]:
    #
    #
    # smd['tagline'] = smd['tagline'].fillna('')
    # smd['description'] = smd['overview'] + smd['tagline']
    # smd['description'] = smd['description'].fillna('')
    #
    #
    # end = time.time()
    # print("smd Creation and Modification: " + str(end - start))
    # # In[32]:
    #
    # #Writing smd to file for future use
    # smd.to_csv("data/smd.txt")
    #Measuring time for performance improvements

    smd = pd.read_csv('data/smd.txt')

    print(type(smd))

    start = time.time()

    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smd['description'].values.astype('U'))

    end = time.time()
    print("tf and tfidf_matrix Creation " + str(end - start))

    # print(type(tfidf_matrix), type(tf), type(smd))

    # In[33]:


    # #### Cosine Similarity
    #
    # I will be using the Cosine Similarity to calculate a numeric quantity that denotes the similarity between two movies. Mathematically, it is defined as follows:
    #
    # $cosine(x,y) = \frac{x. y^\intercal}{||x||.||y||} $
    #
    # Since we have used the TF-IDF Vectorizer, calculating the Dot Product will directly give us the Cosine Similarity Score. Therefore, we will use sklearn's **linear_kernel** instead of cosine_similarities since it is much faster.

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
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


# We're all set. Let us now try and get the top recommendations for a few movies and see how good the recommendations are.

# In[38]:

print("Started")
print(get_recommendations('The Godfather').head(10))
print("Done")


# In[39]:


get_recommendations('The Dark Knight').head(10)
