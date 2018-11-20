# Class to handle hierarchical cluster functionality

# Imports
from utils import Util

class HierchCluster:

  def __init__(self, data, left = None, right = None, distance = 0.0, id = None, name = None):
    self.data = data
    self.left = left
    self.right = right
    self.distance =  distance
    self.id = id
    self.name = name
  
  @staticmethod
  def cluster(data):
    distances = {}
    current_cluster_id = -1

    blogposts = data[0]
    stats = data[2]

    clusters = [HierchCluster(stats[i], id = i, name = blogposts[i]) for i in range(len(stats))]

    while len(clusters) > 1:
      print "Clusters: %d" % len(clusters)
      print current_cluster_id
      
      lowest_pair = (0, 1)
      closest_distance = Util.pearson(clusters[0].data, clusters[1].data)
      
      for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
          if (clusters[i].id, clusters[j].id) not in distances:
            distances[clusters[i].id, clusters[j].id] = Util.pearson(clusters[i].data, clusters[j].data)
          
          current_distance = distances[clusters[i].id, clusters[j].id]

          if (current_distance < closest_distance):
            closest_distance = current_distance
            lowest_pair = (i, j)

      merged_data = [(clusters[lowest_pair[0]].data[i] + clusters[lowest_pair[1]].data[i]) / 2.0 for i in range(len(clusters[0].data))]

      new_cluster = HierchCluster(merged_data, left = clusters[lowest_pair[0]], right = clusters[lowest_pair[1]], distance = closest_distance, id = current_cluster_id)

      current_cluster_id -= 1
      del clusters[lowest_pair[1]]
      del clusters[lowest_pair[0]]
      clusters.append(new_cluster)

    return clusters[0]