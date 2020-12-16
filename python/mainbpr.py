#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:46:51 2020

@author: shah
"""

from filereader import read_ratings, read_movies
from bpr import bpr_update
from hitrate import hit_rate
from random import seed
from util import cov_matrix
from util import random_vector
import numpy as np
import random as random
seed(42)
np.random.seed(42)
print("Reading files...")
users = read_ratings("../data/ratings.csv")
movies = read_movies("../data/movies.csv")
print("Finished Reading files.")
iterations = 10

for i in range(iterations):
    print("Iteration " + str(i))
    bpr_update(users, movies)

print("Finished updating.")
print("Calculating Hit Rate...")

hits, denom, rms, rmsall = hit_rate(users, movies)

print("Trained:")
print("HitRate" + str(hits/denom))
print("Number of Users:" + str(len(users)))
print("Number of Movies:" + str(len(movies)))
