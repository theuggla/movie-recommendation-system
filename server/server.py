# Server starting point

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

# Get the top matching users for the given user
class Matches(Resource):
    def get(self, similarity_measure, user_id):
        similarity = sims.pearson if (similarity_measure == 'pearson') else sims.euclidean
        result = {'data': sims.topMatches(user_id, similarity)}
        return jsonify(result)

# Get movie recommendations for the given user
class Recs(Resource):
    def get(self, similarity_measure, user_id):
        similarity = sims.pearson if (similarity_measure == 'pearson') else sims.euclidean
        result = {'data': recs.getRecommendations(user_id, similarity)}
        return jsonify(result)

# Add resources
api.add_resource(Matches, '/matches/<similarity_measure>/<user_id>') # Route_1
api.add_resource(Recs, '/recommendations/<similarity_measure>/<user_id>') # Route_2


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     