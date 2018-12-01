# Class to handle the ranking functionality

class Metrics:

  def __init__(self, db):
    self.db = db

  # Ranks the pages using the given metrics and returns {url: url, score: score} for each page.
  # Query should be a list of words
  # Metrics should be a list of objects in the form of {metric_function: function, weight: number, prefer_low: boolean}
  def rank(self, pages, query, metrics):
    result = list()
    scores = {}

    for m_idx, metric in enumerate(metrics):
      scores[m_idx] = {}
      for p_idx, page in enumerate(pages):
        scores[m_idx][p_idx] = 0
        score = metric['metric_function'](page, query)
        scores[m_idx][p_idx] = score

    for m_idx, metric in enumerate(metrics):
      scores[m_idx] = self.normalize(scores[m_idx], metric['prefer_low'])

    for p_idx, page in enumerate(pages):
      score = 0
      for m_idx, metric in enumerate(metrics):
        score += (scores[m_idx][p_idx] * metric['weight'])
      result.append({'url': page.url, 'score': score})

    result = sorted(result, key = lambda item: item['score'], reverse = True)

    return result

  # Returns the the word frequency score for the given page and query
  def get_word_frequency_score(self, page, query):
    score = 0

    for part in query:
      word_id = self.db.get_id_for_word(part)
      for word in page.words:
        if word == word_id:
          score += 1

    return float(score)

  # Normalizes a list of scores so that the highest score becomes 1 and the rest are transformed to reflect that
  def normalize(self, scores, low_is_better):
    if len(scores) == 0:
      return scores

    if low_is_better:
      lowest_score = min(scores.values())
      return dict([(page, (lowest_score / max(score, 0,000000000001))) for (page, score) in scores.items()])
    else:
      highest_score = max(scores.values())
      return dict([(page, (score / highest_score)) for (page, score) in scores.items()])
