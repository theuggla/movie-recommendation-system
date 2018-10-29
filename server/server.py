
# Flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

# Local imports
from db import DB
from similarities import Similarities
from recommendations import Recommendations

# Global definitions
db_path = 'db/movies.db'
app = Flask(__name__)
api = Api(app)
db = DB(db_path)
sims = Similarities(db)
recs = Recommendations(db)

class Ratings(Resource):
    def get(self, user_id):
        result = {'pearson': sims.topMatches(user_id, sims.pearson), 'euclidian': sims.topMatches(user_id, sims.euclidean)}
        return jsonify(result)

class Recs(Resource):
    def get(self, user_id):
        result = {'pearson': recs.getRecommendations(user_id, sims.pearson), 'euclidian': recs.getRecommendations(user_id, sims.euclidean)}
        return jsonify(result)

api.add_resource(Ratings, '/ratings/<user_id>') # Route_1
api.add_resource(Recs, '/recommendations/<user_id>') # Route_2


if __name__ == '__main__':
     app.run(port='5002')
     