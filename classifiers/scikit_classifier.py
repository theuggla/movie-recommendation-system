# Imports
from classifier import Classifier
from joblib import dump, load
import numpy as np
import json

class SciKitClassifier(Classifier):

  # Saves the model
  def save(self, name):
    dump(self.model, './data/models/' + name + '.joblib')
    
    with open('./data/models/' + name + '-history.json', 'w') as file:
        json.dump(self.history.tolist(), file)

  # Loads the model
  def load(self, name):
    self.model = load('./data/models/' + name + '.joblib')

    with open('./data/models/' + name + '-history.json') as file:
        self.history = np.array(json.load(file))

  # Trains the model
  def train(self):
    self.model.fit(self.x_train, self.y_train)
    self.history = self.model.predict(self.x_test)

  # Evaluates the model
  def evaluate(self):
    accuracy = self.model.score(self.x_test, self.y_test)
    return accuracy