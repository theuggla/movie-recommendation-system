# Class to handle util functionality

# Imports
import os
from pages import PageDB, Page

class Util:

  # Indexes all the bag-of-words pages from the given directory
  @staticmethod
  def index_pages(directory_path, pageDB):
    for filename in os.listdir(directory_path):
      with open(directory_path + '/' + filename) as f:
        words = [word for line in f for word in line.split()]
        pageDB.add_page('wiki/' + filename, words)
