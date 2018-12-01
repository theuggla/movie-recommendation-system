# Classes to handle page functionality

class PageDB:

  def __init__(self):
    self.word_to_id  = {}
    self.pages = []

  # Adds a page from an url a list of the words in the page, and the links going out from the page
  def add_page(self, url, words, links = []):
    words_as_ids = [self.get_id_for_word(word) for word in words]
    self.pages.append(Page(url, words_as_ids, links))

  # Get a numeric value for the given word
  def get_id_for_word(self, word):
    if word in self.word_to_id:
      return self.word_to_id[word]
    else:
      id = len(self.word_to_id)
      self.word_to_id[word] = id
      return id
  
  # Returns a list of all pages that has all of the given words in them
  def search(self, words):
    result_lists = [(filter(lambda page: self.get_id_for_word(word) in page.words, self.pages)) for word in words]
    results = set(result_lists.pop())
    
    for result in result_lists:
      results = results.intersection(set(result))

    return list(results)

  # Calculates the page rank for each page over the given number of iterations
  def calculate_page_rank(self, iterations):
    for _ in range(iterations):
      for page in self.pages:
        rank = 0
        for other_page in self.pages:
          if page.url != other_page.url:
            if page.url in other_page.links:
              rank += other_page.page_rank / len(other_page.links)

        page.page_rank = (rank * 0.85) + 0.15

class Page:
  
  def __init__(self, url, words_as_ids, links):
    self.url = url
    self.words = words_as_ids
    self.links = links
    self.page_rank = 1.0
