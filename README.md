# Bayesian Personalized Ranking (BPR) in Python

Bayesian Personalized Ranking (BPR) [1] is a recommender systems algorithm that can be used to personalize the experience of a user on a movie rental service, an online book store, a retail store and so on.

This implementation uses the MovieLens data set [2] but the implementation can be used for any recomender system application.

BPR learns latent factors of a user and an item (movie) and based on inner products of user and item embeddings, it ranks movies in the decreasing order of the predicted rating. The algorithm can be used for any application where implicit or explicit preferences of guests are available. The algorithm is similar to collaborative filtering algorithms, and can be used for matrix factorization/completion problems.

BPR puts a zero mean Gaussian prior on the learnt latent factors (embeddings) which results in an L2 regularization term in the loss function (the algorithm performs pretty well even without this extra term).

The implementation requires python3, pandas and numpy. The dimensionality can be changed in util.py. Currently it uses a dimensionality of 50 and 10 iterations. For larger dimensionality and more number of iterations, it might be useful if there is an access to a cluster of servers or a GPU.

The hit rate @ position 10 is around **51%** (on a 30% test set) on the MovieLens [2] data set with 600 users, 9000 movies and 100,000 ratings. The data is uploaded to the data folder for convenience.

The MovieLens data sets can be found on the [MovieLens Web Page](https://grouplens.org/datasets/movielens/).

Usage:
  
    Run: python mainbpr.py
  
    Change the file names in mainbpr.py
  
    The parameters of the algorithm are in util.py

This code is part of a project in the Data Mining course at JHU.

[1] Rendle, Steffen, et al. "BPR: Bayesian personalized ranking from implicit feedback." arXiv preprint arXiv:1205.2618 (2012).

[2] Harper, F. Maxwell, and Joseph A. Konstan. "The movielens datasets: History and context." Acm transactions on interactive intelligent systems (tiis) 5.4 (2015): 1-19.
