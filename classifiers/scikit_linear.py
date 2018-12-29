# Imports
from scikit_classifier import SciKitClassifier
from sklearn import linear_model

class SciKitLinear(SciKitClassifier):

  # Builds the model with defaults parameters max_iterations=1000
  def build(self):
    self.model = linear_model.SGDClassifier(tol=1e-3)