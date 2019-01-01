# Imports
import time
from classifiers.keras_linear import KerasLinear
from classifiers.keras_convnet import KerasConvNet
from classifiers.scikit_linear import SciKitLinear
from classifiers.scikit_nn import SciKitNN
from keras.datasets import mnist
from data import Data
from graph import Graph

# Global variables
data = Data('./data/spiral/spiral.csv')

# Load data
(mnist_x_train, mnist_y_train), (mnist_x_test, mnist_y_test) = mnist.load_data()
(spiral_x_train, spiral_y_train), (spiral_x_test, spiral_y_test) = data.load_data()
(spiral_data), (spiral_values) = data.load_data_full()

# Build and compile networks
k_linear_model = KerasLinear(mnist_x_train, mnist_y_train, mnist_x_test, mnist_y_test, epochs=15)
k_convnet_model = KerasConvNet(mnist_x_train, mnist_y_train, mnist_x_test, mnist_y_test, epochs=10)

sci_linear_model = SciKitLinear(spiral_x_train, spiral_y_train, spiral_x_test, spiral_y_test)
sci_nn_model = SciKitNN(spiral_x_train, spiral_y_train, spiral_x_test, spiral_y_test)

# Train and time linear
print("Training Linear Classifier:")
linear_start = time.time()
k_linear_model.train()
linear_time = time.time() - linear_start

# Train and time cnn
print("Training ConvNet Classifier:")
cnn_start = time.time()
k_convnet_model.train()
cnn_time = time.time() - cnn_start

# Train and time SciKit models
print("Training SciKit Classifiers:")
sci_linear_time_start = time.time()
sci_linear_model.train()
sci_linear_time = time.time() - sci_linear_time_start

sci_nn_time_start = time.time()
sci_nn_model.train()
sci_nn_time = time.time() - sci_nn_time_start

# Save models
sci_linear_model.save('scikit_linear')
sci_nn_model.save('scikit_nn')
k_linear_model.save('keras_linear')
k_convnet_model.save('keras_convnet')

# Print metrics
k_linear_loss, k_linear_accuracy = k_linear_model.evaluate()
k_convnet_loss, k_convnet_accuracy = k_convnet_model.evaluate()
scikit_linear_accuracy = sci_linear_model.evaluate()
scikit_nn_loss, scikit_nn_accuracy = sci_nn_model.evaluate()

print("\n\n---------SCIKIT-SPIRAL----------\n\n")

print("Linear Classifier: ")
print("Test Accuracy   " + str(scikit_linear_accuracy))
print("Test Loss   -")
print("Linear Time   " + str(sci_linear_time))

print('')

print("Neural Network Classifier: ")
print("Test Accuracy   " + str(scikit_nn_accuracy))
print("Test Loss   " + str(scikit_nn_loss))
print("Neural Network Time   " + str(sci_nn_time))

print("\n\n---------SCIKIT-SPIRAL----------\n\n")


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


print("\n\n---------KERAS-MNIST----------\n\n")

print("Linear Classifier:")
print("Test Accuracy   " + str(k_linear_accuracy))
print("Test Loss   " + str(k_linear_loss))
print("Linear Time   " + str(linear_time))

print('')

print("ConvNet Classifier:")
print("Test Accuracy   " + str(k_convnet_accuracy))
print("Test Loss   " + str(k_convnet_loss))
print("ConvNet Time   " + str(cnn_time))

print("\n\n---------KERAS-MNIST----------\n\n")

# Print graphs
scatterplot = Graph.scatterplot(spiral_data, spiral_values, "Spiral Data Scatterplot")
linear_cm = Graph.confusion_matrix(spiral_y_test, sci_linear_model.history, "Scikit Linear Confusion Matrix")
nn_cm = Graph.confusion_matrix(spiral_y_test, sci_nn_model.history, "Scikit Neural Network Confusion Matrix")
keras_plot = Graph.plot_keras(k_linear_model.history, k_convnet_model.history, "Keras Plot")

Graph.show([scatterplot, linear_cm, nn_cm, keras_plot])