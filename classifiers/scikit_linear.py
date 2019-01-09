# Imports
from scikit_classifier import SciKitClassifier
from sklearn import linear_model

class SciKitLinear(SciKitClassifier):

  # Builds the model with defaults parameters
  def build(self):
    self.model = linear_model.SGDClassifier(tol=1e-3)