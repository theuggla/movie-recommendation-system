# Imports
from keras_classifier import KerasClassifier
from keras import optimizers, activations, losses, metrics
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten

class KerasLinear(KerasClassifier):

    def __init__(self, x_train, y_train, x_test, y_test, name=None, batch_size=128, epochs=10):
        KerasClassifier.__init__(self, x_train, y_train, x_test, y_test, name=name, batch_size=batch_size)
        self.epochs = epochs

    def reshape(self):
        KerasClassifier.reshape(self)

    def build(self):
        self.model = Sequential()
        self.model.add(Flatten(input_shape=(28,28)))
        self.model.add(Dense(512, activation=activations.relu))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(512, activation=activations.relu))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(self.classes, activation=activations.softmax))

        self.model.compile(loss=losses.categorical_crossentropy, optimizer=optimizers.SGD(), metrics=[metrics.categorical_accuracy])