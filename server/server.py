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

# Global definitions
app = Flask(__name__, static_url_path = '/server')
api = Api(app)
CORS(app)
pageDB = PageDB()
Util.index_pages('./server/data/Words/Games', pageDB)
Util.index_pages('./server/data/Words/Programming', pageDB)

# Search for a single word in the list
class Search(Resource):
    def get(self, search_term):
        results = pageDB.search(search_term)

        return(jsonify(results))

# Add resources
api.add_resource(Search, '/search/<search_term>') # Route_1


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     