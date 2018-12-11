# Class to handle util functionality

# Imports
<<<<<<< HEAD
from math import sqrt

class Util:

  # Load data from file
  @staticmethod
  def readfile(filename):
    lines = [line for line in file(filename)]

    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []

    for line in lines[1:]:
      columns = line.strip().split('\t')
      rownames.append(columns[0])
      data.append([float(x) for x in columns[1:]])
    
    return rownames, colnames, data

  # Pearson similarity measure
  @staticmethod
  def pearson(stats_a, stats_b):
    a_stats_sum = sum(stats_a)
    b_stats_sum = sum(stats_b)
    
    a_squared_sum = sum([pow(num, 2) for num in stats_a])
    b_squared_sum = sum([pow(num, 2) for num in stats_b])
    
    product_of_stats_sum = sum([stats_a[i] * stats_b[i] for i in range(len(stats_a))])

    nominator = product_of_stats_sum -(a_stats_sum * b_stats_sum / len(stats_a))
    denominator = sqrt((a_squared_sum - pow(a_stats_sum, 2) / len(stats_a)) * (b_squared_sum - pow(b_stats_sum, 2) / len(stats_b)))
    
    if denominator == 0:
      return 0
 
    return 1.0 - (nominator / denominator)
=======
import os
from pages import PageDB, Page

class Util:

  # Indexes all the bag-of-words pages from the given directory
  @staticmethod
  def index_pages(directory_paths, pageDB):
    for filename in os.listdir(directory_paths['articles']):
      with open(directory_paths['articles'] + '/' + filename) as article:
        with open(directory_paths['links'] + '/' + filename) as links:
          words = [word for line in article for word in line.split()]
          links = [link.rstrip() for link in links]
          pageDB.add_page('/wiki/' + filename, words, links)
>>>>>>> search-engine/master
