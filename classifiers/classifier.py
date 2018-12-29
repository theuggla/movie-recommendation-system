# Imports
from abc import ABCMeta, abstractmethod
from joblib import dump, load

# Base class for the classifiers
class Classifier(object):
  __metaclass__ = ABCMeta

  def __init__(self, x_train, y_train, x_test, y_test, name=None):
    self.model = None
     
    self.x_train = x_train
    self.x_test = x_test
        
    self.y_train = y_train
    self.y_test = y_test

    self.reshape()

    if name == None:
      self.build()
    else:
      self.load(name)

  # Default reshape method
  def reshape(self):
    pass

  # Classifier specific build
  @abstractmethod
  def build(self):
    pass

   # Classifier specific train
  @abstractmethod
  def train(self):
    pass

   # Classifier specific evaluate
  @abstractmethod
  def evaluate(self):
    pass

  # Saves the model
  def save(self, name):
    dump(self.model, './data/models/' + name + '.joblib')

  # Loads the model
  def load(self, name):
    self.model = load('./data/models/' + name + '.joblib')
