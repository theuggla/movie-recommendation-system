# Imports
import matplotlib.pyplot as plt
import numpy as np

class Graph:
  
  @staticmethod
  def scatterplot(points, labels):
    x_points = [point[0] for point in points]
    y_points = [point[1] for point in points]
    
    plt.xlabel('x')
    plt.ylabel('y')

    plt.scatter(x_points, y_points, c=labels)
    cb = plt.colorbar()
    cb.set_ticks(np.unique(labels))
    cb.set_ticklabels(np.unique(labels.astype('int32')))
    plt.show()