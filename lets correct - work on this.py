import pandas as pd
import numpy as np
import turicreate as tc

import numpy as np
import scipy
import math
import random

import sklearn
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extrqction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse.linalg import svds














users = pd.read_csv('lucid blog.csv/users.csv')
users.head()

lucid_tfidf = TfidVectorizer(stopwords='English')
users['short_bio'] = users['short_bio'].fillna('')
u_matx = lucid_tfidf.fit_transform(users['short_bio'])

u_matx.shape

cosine_similarity = linear_kernel(u_matx, u_matx)

indices = pd.Series(users['name'].index)

def recommend(index, cosine_sim=cosine_similarity):
    id = indices[index]
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]

    lud_index = [i[0] for i in similarity_scores]

    return users['name'].iloc[lud_index]

recommend(2)

recommend(6)


posts = pd.read_csv('lucid blog.csv/posts.csv')
posts.head()

lucids_tfidf = TfidVectorizer(stopwords='English')
posts['title'] = posts['title'].fillna('')
p_matx = lucids_tfidf.fit_transform(posts['title'])

p_matx.shape

cosine_similarity = linear_kernel(p_matx, p_matx)

indicesz = pd.Series(posts['content'].index)

def recommend(index, cosine_sim=cosine_similarity):
    id = indicesz[index]
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]

    lud_index = [i[0] for i in similarity_scores]

    return posts['content'].iloc[lud_index]

recommend(6)

recommend(10)


notifications = pd.read_csv('lucid blog.csv/notifications.csv')
notifications.head()

lucidss_tfidf = TfidVectorizer(stopwords='English')
notifications['comment'] = notifications['comment'].fillna('')
n_matx = lucidss_tfidf.fit_transform(notifications['comment'])

n_matx.shape

cosine_similarity = linear_kernel(n_matx, n_matx)

indiceszs = pd.Series(notifications['post_id'].index)

def recommend(index, cosine_sim=cosine_similarity):
    id = indiceszs[index]
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]

    lud_index = [i[0] for i in similarity_scores]

    return notifications['post_id'].iloc[lud_index]

recommend(10)

recommend(14)
