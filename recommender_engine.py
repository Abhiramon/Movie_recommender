from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
import scipy.sparse
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

# from surprise import Reader, Dataset, SVD, evaluate

import warnings; warnings.simplefilter('ignore')



def get_recommendations(title, number_of_recommendations):

    smd = pd.read_csv('data/smd.txt')


    tfidf_matrix = scipy.sparse.load_npz('data/tfidf_matrix.npz')

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    # cosine_sim = np.load('data/cosine_sim.npy')


    # We now have a pairwise cosine similarity matrix for all the movies in our dataset. The next step is to write a function that returns the 30 most similar movies based on the cosine similarity score.



    smd = smd.reset_index()
    titles = smd['title']
    # indices = pd.Series(smd.index, index=smd['title'])
    indices = dict(list(zip(smd['title'], smd.index)))

    # Creates a Levenshtein distance score list
    title_fuzzy_scores = [[fuzz.ratio(title.lower(), list_title.lower()) + fuzz.partial_ratio(title.lower(), list_title.lower()), list_title] for list_title in titles]

    #Sort score in descending order
    sorted_title_fuzzy_scores = sorted(title_fuzzy_scores, key = lambda x: x[0], reverse=True)

    # print(sorted_title_fuzzy_scores[0:20])

    #Choose best match to the title given by the user
    best_match_title = sorted_title_fuzzy_scores[0][1]

    # print(best_match_title)
    #Search titles for the matched title

    idx = indices[best_match_title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    # print(sim_scores)

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    #Select from 1 to exclude the title
    sim_scores = sim_scores[1:number_of_recommendations + 1]

    movie_indices = [i[0] for i in sim_scores]



    return titles.iloc[movie_indices]



# if __name__ == "__main__":
    # print(get_recommendations('The Godfather', 5)
    #
    #
    # get_recommendations('The Dark Knight', 5)
