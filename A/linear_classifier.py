# Imports
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras import optimizers
from keras.utils import np_utils

class Linear:

    # Classifier specifics
    batch_size = 128
    epochs = 15

    # MNIST specifics
    classes = 10 # Numbers 0-9
    input_dimension = 784 # 28x28 px per image
    train_count = 60000
    test_count = 10000

    def __init__(self, x_train, y_train, x_test, y_test):
        self.model = None
        self.history = None
        self.evaluation = None

        # Reshape data as MNIST to use with the linear classifier, cast to float and normalize to a number between 0.0 and 1.0        
        self.x_train = x_train / 255.0
        self.x_test = x_test / 255.0
        
        # Convert integer targets into categorical targets for use with the categorical loss-function
        self.y_train = np_utils.to_categorical(y_train, self.classes)
        self.y_test = np_utils.to_categorical(y_test, self.classes)

        self.build()


    def build(self):
        self.model = Sequential()
        self.model.add(Flatten(input_shape=(28,28)))
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(self.classes, activation='softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(), metrics=['accuracy'])

    def train(self):
      self.history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs, validation_data=(self.x_test, self.y_test))

    def evaluate(self):
      self.evaluation = self.model.evaluate(self.x_test, self.y_test)
      return self.evaluation[1]