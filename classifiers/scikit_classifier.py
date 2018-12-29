# Imports
from classifier import Classifier

class SciKitClassifier(Classifier):

  # Trains the model
  def train(self):
    self.model.fit(self.x_train, self.y_train)

  # Evaluates the model
  def evaluate(self):
    accuracy = self.model.score(self.x_test, self.y_test)
    return accuracy