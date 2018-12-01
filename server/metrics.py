# Class to handle the ranking functionality

class Metrics:

  # Ranks the pages using the given metrics and returns {url: url, score: score} for each page.
  # Query should be a list of words
  # Metrics should be a list of objects in the form of {metric_function: function, weight: number, prefer_low: boolean}
  @staticmethod
  def rank(pages, query, metrics):
    result = list()
    scores = {}

    for page in pages:
      
      scores[page] = 0
      
      for metric in metrics:
        score = Metrics.normalize(metric.metric_function(page, query), metric.prefer_low) * metric.weight
        scores[page] += score

      result.append({'url': page.url, 'score': scores[page]})

    return result

  # Returns the the word frequency score for the given page and query
  @staticmethod
  def get_word_frequency_score(page, query):
    return

  @staticmethod
  def normalize(score, low_is_better):
    return