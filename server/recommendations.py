class Recommendations:
  def __init__(self, db):
    self.db = db

  def getRecommendations(self, person, similarity):
    totals = {}
    simSums = {}

    users = self.db.get_all_user_ids()
    
    for other in users:
      if int(other) == int(person):
        continue

      sim = similarity(person, other)

      if sim <= 0:
        continue
      
      other_ratings = self.db.get_ratings_for(other)
      person_ratings =self.db.get_ratings_for(person)
    
      for rating_o in other_ratings:
        alreadySeen = False
        
        for rating_p in person_ratings:
          if (rating_o["Movie"] == rating_p["Movie"]) and int(rating_p["Rating"]) != 0:
            alreadySeen = True
        
        if alreadySeen:
          continue
        
        totals.setdefault(rating_o["Movie"], 0)
        totals[rating_o["Movie"]] += rating_o["Rating"] * sim

        simSums.setdefault(rating_o["Movie"], 0)
        simSums[rating_o["Movie"]] += sim

    rankings=[(total/simSums[item],item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings