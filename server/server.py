# Server starting point

# Flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS

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

CORS(app)

# Get the users
class Users(Resource):
    def get(self):
        composed_users = []
        users = db.get_all_users()
        
        for user in users:
            user['Ratings'] = db.get_ratings_for(user['UserID'])
            composed_users.append(user)
            
        result = composed_users
        return jsonify(result)

# Get the top matching users for the given user
class Matches(Resource):
    def get(self, similarity_measure, user_id):
        similarity = sims.pearson if (similarity_measure == 'pearson') else sims.euclidean
        result = sims.topMatches(user_id, similarity)
        return jsonify(result)

# Get movie recommendations for the given user
class Recs(Resource):
    def get(self, similarity_measure, user_id):
        similarity = sims.pearson if (similarity_measure == 'pearson') else sims.euclidean
        result = recs.getRecommendations(user_id, similarity)
        return jsonify(result)

# Add resources
api.add_resource(Matches, '/matches/<similarity_measure>/<user_id>') # Route_1
api.add_resource(Recs, '/recommendations/<similarity_measure>/<user_id>') # Route_2
api.add_resource(Users, '/users') # Route_3


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     