# Imports
from sklearn.metrics import confusion_matrix
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools
import numpy as np
import math

class Graph:
  
  @staticmethod
  def scatterplot(points, labels, title):
    scatterplot = plt.figure(num=title, clear=True)

    for lbl in np.unique(labels):
      x_points = np.array([point[0] for index, point in enumerate(points) if labels[index] == lbl])
      y_points = np.array([point[1] for index, point in enumerate(points) if labels[index] == lbl])

      top = max(labels) + 0.4
      r = lbl
      b = lbl + 0.2
      g = lbl + 0.4
      color = (r / top, b / top, g / top)

      plt.scatter(x_points, y_points, c=color, label=lbl.astype('int32'))
      
    plt.xlabel('X')
    plt.ylabel('Y', rotation='0')
    plt.title(title)
    plt.legend(scatterpoints=1, title="Classes", fancybox=True)
    
    plt.tight_layout()
    return plt.figure(num=title)



  @staticmethod
  def confusion_matrix(y_test, y_pred, title):
    confusion_plot = plt.figure(num=title, clear=True)
    
    cm = confusion_matrix(y_test, y_pred)
    labels = np.unique(y_test).astype('int32')

    plt.imshow(cm, cmap=plt.cm.Blues)
    plt.title(title)
    
    cb = plt.colorbar()
    cb.set_ticks(range(0, 11, 2))
    cb.set_ticklabels(range(0, 11, 2))
    plt.clim(0, 10);
    
    tick_marks = np.arange(len(labels))
    plt.yticks(tick_marks, labels)
    plt.ylabel('True label')
    plt.xticks(tick_marks, labels)
    plt.xlabel('Predicted label')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    return confusion_plot

  @staticmethod
  def plot_keras(linear_history, nn_history, title):
    keras_plot = plt.figure(num=title, clear=True)

    linear_epochs = len(linear_history.epoch)
    conv_net_epochs = len(nn_history.epoch)

    # Accuracy subplot
    plt.subplot(2, 1, 1)
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')

    tick_marks = np.arange(max(conv_net_epochs, linear_epochs))
    plt.xticks(tick_marks, range(1, max(conv_net_epochs, linear_epochs) + 1))

    cmap = plt.cm.get_cmap('Set3')

    for index, key in enumerate(linear_history.history):
      if key.find('accuracy') != -1:
        c = cmap(float(index)/(10-1))
        c2 = cmap(float(index * 2)/(10-1))
        plt.plot(linear_history.history[key], label='Linear ' + ('Test' if 'val' in key else 'Training') + ' Accuracy', color = c)
        plt.plot(nn_history.history[key], label='ConvNet ' + ('Test' if 'val' in key else 'Training') + ' Accuracy', color = c2)

    plt.legend()

    # Accuracy subplot
    plt.subplot(2, 1, 2)
    plt.title('Model Loss')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')

    tick_marks = np.arange(max(conv_net_epochs, linear_epochs))
    plt.xticks(tick_marks, range(1, max(conv_net_epochs, linear_epochs) + 1))

    cmap = plt.cm.get_cmap('Accent')
    
    for index, key in enumerate(linear_history.history):
      if key.find('loss') != -1:
        c = cmap(float(index)/(10-1))
        c2 = cmap(float(index * 2)/(10-1))
        plt.plot(linear_history.history[key], label='Linear ' + ('Test' if 'val' in key else 'Training') + ' Loss', color = c)
        plt.plot(nn_history.history[key], label='ConvNet ' + ('Test' if 'val' in key else 'Training') + ' Loss', color = c2)

    plt.legend()

    plt.tight_layout()

    return keras_plot

  @staticmethod
  def show(figures):
    plt.show(figures)