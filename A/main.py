# Imports
import time

from linear_classifier import Linear
from keras.datasets import mnist

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Build and compile networks
linear_model = Linear(x_train, y_train, x_test, y_test)

# Time linear
linear_start = time.time()
linear_model.train()
linear_time = time.time() - linear_start

# Print metrics
accuracy = linear_model.evaluate()

print("Linear Classifier:")
print("Test Accuracy   " + str(accuracy))
print("Linear Time   " + str(linear_time))
