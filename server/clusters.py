# Class to handle cluster functionality

class Clusters:

  # Load data from file
  def readfile(self, filename):
    lines = [line for line in file(filename)]

    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []

    for line in lines[1:]:
      columns = line.strip().split('\t')
      rownames.append(columns[0])
      data.append([float(x) for x in columns[1:]])
    
    return rownames, colnames, data