# Server starting point

# Flask imports
from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS

# Local imports
from utils import Util
from pages import PageDB
from metrics import Metrics

# Global definitions
app = Flask(__name__, static_url_path = '/server')
api = Api(app)
CORS(app)
pageDB = PageDB()
Util.index_pages('./server/data/Words/Games', pageDB)
Util.index_pages('./server/data/Words/Programming', pageDB)

# Search for a single word in the list
class Search(Resource):
    def get(self, rank_type):
        query = request.query_string.split('+')
        results = pageDB.search(query)
        metrics = {'metric_function': Metrics.get_word_frequency_score, 'weight': 1.0, 'prefer_low': False}
        ranked_results = Metrics.rank(results, query, metrics)

        return(jsonify(ranked_results))

# Add resources
api.add_resource(Search, '/search/<rank_type>') # Route_1


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     