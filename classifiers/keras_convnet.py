# Imports
from keras_classifier import KerasClassifier
from keras import optimizers, activations, losses, metrics
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D


class KerasConvNet(KerasClassifier):

    # MNIST specifics
    img_rows, img_cols = 28, 28
    color_channels = 1
    input_shape = (img_rows, img_cols, 1)

    def __init__(self, x_train, y_train, x_test, y_test, name=None, batch_size=128, epochs=10):
        KerasClassifier.__init__(self, x_train, y_train, x_test, y_test, name=name, batch_size=batch_size)
        self.epochs = epochs
    
    def reshape(self):
        KerasClassifier.reshape(self)

        # Reshape data as MNIST in the form of (number_of_samples, rows, columns, channels)
        self.x_train = self.x_train.reshape(self.train_count, self.img_rows, self.img_cols, self.color_channels)
        self.x_test = self.x_test.reshape(self.test_count, self.img_rows, self.img_cols, self.color_channels)

    def build(self):
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=5, activation=activations.relu, input_shape=self.input_shape))
        self.model.add(MaxPooling2D())
        self.model.add(Conv2D(64, kernel_size=5, activation=activations.relu))
        self.model.add(MaxPooling2D())
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(units=128, activation=activations.relu))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(self.classes, activation=activations.softmax))

        self.model.compile(loss=losses.categorical_crossentropy, optimizer=optimizers.Adadelta(), metrics=[metrics.categorical_accuracy])
