# Imports
from keras.utils import np_utils
from classifier import Classifier

class KerasClassifier(Classifier):

    # MNIST specifics
    classes = 10 # Numbers 0-9
    train_count = 60000
    test_count = 10000

    def __init__(self, x_train, y_train, x_test, y_test, name=None, batch_size=128):
      Classifier.__init__(self, x_train, y_train, x_test, y_test, name=name)
      self.batch_size = batch_size

    def reshape(self):
      # Reshape data, cast to float and normalize to a number between 0.0 and 1.0 
      self.x_train = self.x_train.astype('float32') / 255
      self.x_test = self.x_test.astype('float32') / 255

      # Convert integer targets into categorical targets for use with the categorical loss-function
      self.y_train = np_utils.to_categorical(self.y_train, self.classes)
      self.y_test = np_utils.to_categorical(self.y_test, self.classes)

    def train(self):
      self.history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs, validation_data=(self.x_test, self.y_test))

    def evaluate(self):
      self.evaluation = self.model.evaluate(self.x_test, self.y_test)
      return self.evaluation