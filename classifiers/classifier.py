# Imports
from abc import ABCMeta, abstractmethod

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
  @abstractmethod
  def save(self, name):
    pass

  # Loads the model
  @abstractmethod
  def load(self, name):
    pass
