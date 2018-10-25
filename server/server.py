
# Flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

# Local imports
from db import DB
from similarities import Similarities

# Global definitions
db_path = 'db/movies.db'
app = Flask(__name__)
api = Api(app)
db = DB(db_path)
sims = Similarities(db)

class Ratings(Resource):
    def get(self, user_id):
        result = {'pearson': sims.topMatches(user_id, sims.pearson), 'euclidian': sims.topMatches(user_id, sims.euclidean)}
        return jsonify(result)

api.add_resource(Ratings, '/ratings/<user_id>') # Route_1


if __name__ == '__main__':
     app.run(port='5002')
     