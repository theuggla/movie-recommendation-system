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
game_directories = {'articles': './server/data/Words/Games', 'links': './server/data/Links/Games'}
programming_directories = {'articles': './server/data/Words/Programming', 'links': './server/data/Links/Programming'}
app = Flask(__name__, static_url_path = '/server')
api = Api(app)
CORS(app)
pageDB = PageDB()
Util.index_pages(game_directories, pageDB)
Util.index_pages(programming_directories, pageDB)
metrics = Metrics(pageDB)

# Search for a single word in the list
class Search(Resource):
    def get(self, rank_type):
        query = request.query_string.split('+')
        results = pageDB.search(query)

        if len(results) == 0:
            return (jsonify([]))
        else:
            metrics_to_use = []
            
            if 'wfm' in rank_type:
                metrics_to_use.append({'metric_function': metrics.get_word_frequency_score, 'weight': 1.0, 'prefer_low': False})
            if 'dlm' in rank_type:
                metrics_to_use.append({'metric_function': metrics.get_document_location_score, 'weight': 0.8, 'prefer_low': True})
            
            ranked_results = metrics.rank(results, query, metrics_to_use)
            return (jsonify(ranked_results))

# Add resources
api.add_resource(Search, '/search/<rank_type>') # Route_1


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     