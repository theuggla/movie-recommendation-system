# Class to handle util functionality

# Imports
import os
from pages import PageDB, Page

class Util:

  # Indexes all the bag-of-words pages from the given directory
  @staticmethod
  def index_pages(directory_paths, pageDB):
    for filename in os.listdir(directory_paths['articles']):
      with open(directory_paths['articles'] + '/' + filename) as article:
        with open(directory_paths['links'] + '/' + filename) as links:
          words = [word for line in article for word in line.split()]
          links = [link.rstrip() for link in links]
          pageDB.add_page('wiki/' + filename, words, links)
