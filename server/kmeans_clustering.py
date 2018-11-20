# Class to handle KMeans cluster functionality

# Imports
import random
from utils import Util

class KMeansCluster:

  def __init__(self, num, attributes, stats):
    self.centoid = []
    self.assignments = []
    self.num = num
    self.attributes = attributes
    for index in range(len(attributes)):
      self.centoid.append(random.choice([item[index] for item in stats]))

  def assign(self, assignee):
    self.assignments.append(assignee)
    
  def clear_assignments(self):
    self.assignments = []

  def update_centoid(self):
    centoid = []
    for i in range(len(self.attributes)):
      sum_attr = sum([assignee['stats'][i] for assignee in self.assignments])
      average = sum_attr / len(self.assignments)
      centoid.append(average)
    self.centoid = centoid

  @staticmethod
  def get_clusters(k, attributes, stats):
    return [KMeansCluster(i + 1, attributes, stats) for i in range(k)]

  @staticmethod
  def find_closest(clusters, assignee):
    pearsons = []
    
    for cluster in clusters:
      pearsons.append(Util.pearson(cluster.centoid, assignee['stats']))
    
    return clusters[pearsons.index(min(pearsons))]
  
  @staticmethod
  def run_assignments(data, number_of_clusters, number_of_iterations):
    blogposts = data[0]
    words = data[1]
    stats = data[2]

    clusters = KMeansCluster.get_clusters(number_of_clusters, words, stats)

    i = 0
    no_reassignments = False

    while (no_reassignments == False and (number_of_iterations == False or i < number_of_iterations)):
      print "Iteration %d" % i
      old_assignments = {}
      
      for cluster in clusters:
        old_assignments[cluster.num] = ([assignment['blog'] for assignment in cluster.assignments])
        cluster.clear_assignments()

      for index, blog in enumerate(blogposts):
        assignee = {}
        assignee['blog'] = blog
        assignee['words'] = words
        assignee['stats'] = stats[index]

        closest_cluster = KMeansCluster.find_closest(clusters, assignee)
        closest_cluster.assign(assignee)

      for cluster in clusters:
        cluster.update_centoid()

      for cluster in clusters:
        no_reassignments = (set([assignment['blog'] for assignment in cluster.assignments]) == set(old_assignments[cluster.num]))

        if no_reassignments == False:
          break
      
      i += 1

    return clusters