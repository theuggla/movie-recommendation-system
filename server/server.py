# Server starting point

# Flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS

# Global definitions
app = Flask(__name__)
api = Api(app)
CORS(app)

# Get the users
class Root(Resource):
    def get(self):
        result = {'message': 'connected'}
        return jsonify(result)

# Add resources
api.add_resource(Root, '/') # Route_1


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     