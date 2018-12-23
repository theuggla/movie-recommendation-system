# Imports
import sys, argparse

from sklearn import linear_model
import numpy
from joblib import dump, load

# Command line parser
def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--data',
                    required=True,
                    type=str,
                    dest="data_file",
                    metavar="<path to data>",
                    help="The path to the file to load the data from" )
  parser.add_argument('-m', '--model',
                    required=False,
                    type=str,
                    default="default_model", 
                    dest="model",
                    metavar="<model>",
                    help="Model to load. If empty or non-existant, will save new model under given or default name" )
  parser.add_argument('-t', '--train',
                    required=False,
                    type=bool,
                    default=True, 
                    dest="train",
                    metavar="<train model>",
                    help="Indicate wether the model should be trained" )
  return parser

# Retrieves 90% of the data from the file
def get_training_data(path_to_file):
  training_data = numpy.loadtxt(path_to_file, delimiter=',', usecols=(0, 1), skiprows=1).tolist()
  target_values = numpy.loadtxt(path_to_file, delimiter=',', usecols=(2), skiprows=1).tolist()

  del training_data[0::10]
  del target_values[0::10]
  
  return numpy.array(training_data), numpy.array(target_values)
  
# Retrieves the remaining 10% of data from the file
def get_test_data(path_to_file):
  training_data = numpy.loadtxt(path_to_file, delimiter=',', usecols=(0, 1), skiprows=1)
  target_values = numpy.loadtxt(path_to_file, delimiter=',', usecols=(2), skiprows=1)
  
  test_data = numpy.array(training_data[0::10])
  test_values = numpy.array(target_values[0::10])

  return test_data, test_values

# Trains the model
def train_model(model, X, Y):
  model.fit(X, Y)

# Tests the trained model on the given test data, prints result and accuracy score
def test_model(model, test_data, test_values):
  print('model classification of test data: ')
  print(model.predict(test_data))

  print('correct classification of test data: ')
  print(test_values)

  score = model.score(test_data, test_values)
  print('accuracy score: ' + str(score))

# Saves the model
def save_model(model, name):
  dump(model, './classifiers/' + name + '.joblib')

# Creates or loads, trains, tests, and saves a model
def main(argv):
  parser = create_parser()
  args = parser.parse_args()

  try:
    model = load(args.model + '.joblib')
  except:
    model = linear_model.SGDClassifier(max_iter=1000, tol=1e-3)

  if args.train:
    x, y = get_training_data(args.data_file)
    train_model(model, x, y)

  test_data, test_values = get_test_data(args.data_file)
  test_model(model, test_data, test_values)

  save_model(model, args.model)
  
# Main
if __name__ == "__main__":
   main(sys.argv[1:])

