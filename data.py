# Imports
import numpy

# Class to load and format data
class Data:

  # Spiral specifics
  x_cols = (0, 1)
  y_cols = (2)

  def __init__(self, path_to_file, delimeter = ',', heading_rows = True):
    self.path_to_file = path_to_file
    self.delimeter = delimeter

    if (heading_rows == True):
      self.heading_rows = 1
    else:
      self.heading_rows = 0

  # Loads the data from the file separated into training and test batches
  def load_data(self):
    training_data = self.get_training_data()
    test_data = self.get_test_data()

    return training_data, test_data

  # Loads all the data from the file
  def load_data_full(self):
    return self.get_all_data()

  # Retrieves 90% of the data from the file
  def get_training_data(self):
    training_data = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.x_cols, skiprows=self.heading_rows).tolist()
    target_values = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.y_cols, skiprows=self.heading_rows).tolist()

    del training_data[0::10]
    del target_values[0::10]
    
    return numpy.array(training_data), numpy.array(target_values)
  
  # Retrieves the remaining 10% of data from the file
  def get_test_data(self):
    training_data = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.x_cols, skiprows=self.heading_rows)
    target_values = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.y_cols, skiprows=self.heading_rows)
    
    test_data = numpy.array(training_data[0::10])
    test_values = numpy.array(target_values[0::10])

    return test_data, test_values

  # Retrieves all the data from the file
  def get_all_data(self):
    data = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.x_cols, skiprows=self.heading_rows)
    values = numpy.loadtxt(self.path_to_file, delimiter=self.delimeter, usecols=self.y_cols, skiprows=self.heading_rows)

    return data, values