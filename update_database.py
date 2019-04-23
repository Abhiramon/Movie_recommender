import time
import numpy as np
import pandas as pd


def update_database():
    md = pd. read_csv('data/movies_metadata.csv')


    # In[26]:
    #Measuring time for performance improvements
    start = time.time()

    md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

    end = time.time()
    print("md Creation: " + str(end - start))
    # ## Content Based Recommender
    #
    # The recommender we built in the previous section suffers some severe limitations. For one, it gives the same recommendation to everyone, regardless of the user's personal taste. If a person who loves romantic movies (and hates action) were to look at our Top 15 Chart, s/he wouldn't probably like most of the movies. If s/he were to go one step further and look at our charts by genre, s/he wouldn't still be getting the best recommendations.
    #
    # For instance, consider a person who loves *Dilwale Dulhania Le Jayenge*, *My Name is Khan* and *Kabhi Khushi Kabhi Gham*. One inference we can obtain is that the person loves the actor Shahrukh Khan and the director Karan Johar. Even if s/he were to access the romance chart, s/he wouldn't find these as the top recommendations.
    #
    # To personalise our recommendations more, I am going to build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as **Content Based Filtering.**
    #
    # I will build two Content Based Recommenders based on:
    # * Movie Overviews and Taglines
    # * Movie Cast, Crew, Keywords and Genre
    #
    # Also, as mentioned in the introduction, I will be using a subset of all the movies available to us due to limiting computing power available to me.

    # In[27]:
    #Measuring time for performance improvements
    start = time.time()

    links_small = pd.read_csv('data/links_small.csv')
    links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')

    end = time.time()
    print("links_small Creation: " + str(end - start))




    # In[28]:


    md = md.drop([19730, 29503, 35587])


    # In[29]:


    #Check EDA Notebook for how and why I got these indices.
    md['id'] = md['id'].astype('int')


    # In[30]:
    #Measuring time for performance improvements
    start = time.time()


    smd = md[md['id'].isin(links_small)]


    # We have **9099** movies avaiable in our small movies metadata dataset which is 5 times smaller than our original dataset of 45000 movies.

    # ### Movie Description Based Recommender
    #
    # Let us first try to build a recommender using movie descriptions and taglines. We do not have a quantitative metric to judge our machine's performance so this will have to be done qualitatively.

    # In[31]:


    smd['tagline'] = smd['tagline'].fillna('')
    smd['description'] = smd['overview'] + smd['tagline']
    smd['description'] = smd['description'].fillna('')


    end = time.time()
    print("smd Creation and Modification: " + str(end - start))
    # In[32]:

    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smd['description'].values.astype('U'))

    print(type(tfidf_matrix))

    scipy.sparse.save_npz('data/tfidf_matrix.npz', tfidf_matrix)
    #Writing smd to file for future use
    smd.to_csv("data/smd.txt")
