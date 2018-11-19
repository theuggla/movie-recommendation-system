# Class to calculate similarity scores between users uing different algorithms

# Imports
from math import sqrt

class Similarities:
  def __init__(self, db):
    self.db = db

  # Euclidian similarity measure
  def euclidean(self, person_a_id, person_b_id):
    similarity = 0
    ratings_in_common = 0

    person_a_ratings = self.db.get_ratings_for(str(person_a_id))
    person_b_ratings = self.db.get_ratings_for(str(person_b_id))
  
    for ratingA in person_a_ratings:
      for ratingB in person_b_ratings:
        if (ratingA['Movie'] == ratingB['Movie']):
          similarity += pow(ratingA['Rating'] - ratingB['Rating'], 2)
          ratings_in_common += 1
    
    if ratings_in_common == 0:
      return 0
    
    inverted_similarity = 1 / (1 + similarity)
    return inverted_similarity

  # Pearson similarity measure
  def pearson(self, person_a_id, person_b_id):
    a_scores = 0
    b_scores = 0
    a_squared = 0
    b_squared = 0
    product_of_scores = 0
    ratings_in_common = 0

    person_a_ratings = self.db.get_ratings_for(str(person_a_id))
    person_b_ratings = self.db.get_ratings_for(str(person_b_id))
    
    for ratingA in person_a_ratings:
      for ratingB in person_b_ratings:
        if ratingA["Movie"] == ratingB["Movie"]:
          ratings_in_common += 1
          a_scores += ratingA["Rating"]
          b_scores += ratingB["Rating"]
          a_squared += pow(ratingA["Rating"], 2)
          b_squared += pow(ratingB["Rating"], 2)
          product_of_scores += ratingA['Rating'] * ratingB['Rating']

    if ratings_in_common == 0: 
      return 0

    nominator = product_of_scores -(a_scores * b_scores / ratings_in_common)
    denominator = sqrt((a_squared - pow(a_scores, 2) / ratings_in_common) * (b_squared - pow(b_scores, 2) / ratings_in_common))
    
    if denominator == 0:
      return 0
 
    return nominator / denominator

  # Gets the top-similarity matches for the given user
  def topMatches(self, person, similarity, number_of_matches = 5):
    users = self.db.get_all_user_ids()

    scores = [(similarity(person, other), self.db.get_name_from_id(other))
              for other in users if other != int(person)]

    scores.sort( )
    scores.reverse( )
    return scores[0:number_of_matches]