# BPR
## Implementation of Bayesian Personalized Ranking [1] in Python

Bayesian Personalized Ranking (BPR) is a recommender systems algorithm that can be used to personalize the experience of a user on a movie rental service, an online book store, a retail store and so on.

This implementation uses the MovieLens data set [2] but the implementation can be used for any recomender system application.

BPR leanrs latent factors of a user and an item (movie) and based on inner products of user and item embeddings, it ranks movies in the decreasing order of the predicted rating. The algorithm can be used for any application where implicit or explicit preferences of guests are available.

BPR puts a zero mean Gaussian prior on the learnt latent factors (embeddings) which results in an L2 regularization term in the loss function.

[1] Rendle, Steffen, et al. "BPR: Bayesian personalized ranking from implicit feedback." arXiv preprint arXiv:1205.2618 (2012).

[2] Harper, F. Maxwell, and Joseph A. Konstan. "The movielens datasets: History and context." Acm transactions on interactive intelligent systems (tiis) 5.4 (2015): 1-19.
