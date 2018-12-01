# Classes to handle page functionality

class PageDB:

  def __init__(self):
    self.word_to_id  = {}
    self.pages = []

  # Adds a page from an url and a list of the words in the page
  def add_page(self, url, words):
    words_as_ids = [self.get_id_for_word(word) for word in words]
    self.pages.append(Page(url, words_as_ids))

  # Get a numeric value for the given word
  def get_id_for_word(self, word):
    if word in self.word_to_id:
      return self.word_to_id[word]
    else:
      id = len(self.word_to_id)
      self.word_to_id[word] = id
      return id
  
  # Returns a list of all pages that has the given word in them
  def search(self, word):
    results = list(filter(lambda page: self.get_id_for_word(word) in page.words, self.pages))
    return [{'url': page.url} for page in results]



class Page:
  
  def __init__(self, url, words_as_ids):
    self.url = url
    self.words = words_as_ids
