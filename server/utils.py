# Class to handle util functionality

# Imports
from math import sqrt
from collections import Counter, defaultdict
import os

class Util:

  # Create word list
  @staticmethod
  def get_total_occurences_of_words(directory_path):
    total = defaultdict(lambda: 1.0)

    for file in os.listdir(directory_path):
      with open(directory_path + '/' + file) as article:
        words = [word for line in article for word in line.split()]
        occurences = Counter(words)

        for word, count in occurences.items():
          total[word] += float(count)

    return dict(total)


  # Create word list
  @staticmethod
  def generate_word_list(directory_paths):
    gaming_total = Util.get_total_occurences_of_words(directory_paths['gaming'])
    programming_total = Util.get_total_occurences_of_words(directory_paths['programming'])

    word_list = {}

    for word in programming_total:
      if word in gaming_total:
        word_list[word] =float( min(programming_total[word], gaming_total[word]) ) / float( max(programming_total[word], gaming_total[word]) )
      else:
        word_list[word] = 1.0 / float( programming_total[word] )

    for word in gaming_total:
      if word not in word_list:
        word_list[word] = 1.0 / float( gaming_total[word] )
    
    sorted_word_list = sorted(word_list.items(), key = lambda kv: kv[1])

    return dict(sorted_word_list[:100]).keys()

  # Create word list file
  @staticmethod
  def createfile(filename, wordlist, directory_path, overwrite = False):
    if overwrite:
      with open(filename, "w") as f:
        f.write('Article\t')
        for word in wordlist:
          f.write(word + '\t')
        f.write('\n')
        
        for file in os.listdir(directory_path):
          with open(directory_path + '/' + file) as article:
            f.write(file + '\t')
            words = [word for line in article for word in line.split()]
            for word in wordlist:
              f.write(str(words.count(word)) + '\t')
            f.write('\n')
    else:
      with open(filename, "a") as f:
        for file in os.listdir(directory_path):
            with open(directory_path + '/' + file) as article:
              f.write(file + '\t')
              words = [word for line in article for word in line.split()]
              for word in wordlist:
                f.write(str(words.count(word)) + '\t')
              f.write('\n')
          

  # Load data from file
  @staticmethod
  def readfile(filename):
    lines = [line for line in file(filename)]

    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []

    for line in lines[1:]:
      columns = line.strip().split('\t')
      rownames.append(columns[0])
      data.append([float(x) for x in columns[1:]])
    
    return rownames, colnames, data

  # Pearson similarity measure
  @staticmethod
  def pearson(stats_a, stats_b):
    a_stats_sum = sum(stats_a)
    b_stats_sum = sum(stats_b)
    
    a_squared_sum = sum([pow(num, 2) for num in stats_a])
    b_squared_sum = sum([pow(num, 2) for num in stats_b])
    
    product_of_stats_sum = sum([stats_a[i] * stats_b[i] for i in range(len(stats_a))])

    nominator = product_of_stats_sum -(a_stats_sum * b_stats_sum / len(stats_a))
    denominator = sqrt((a_squared_sum - pow(a_stats_sum, 2) / len(stats_a)) * (b_squared_sum - pow(b_stats_sum, 2) / len(stats_b)))
    
    if denominator == 0:
      return 0
 
    return 1.0 - (nominator / denominator)