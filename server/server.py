# Server starting point

# Flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS

# Local imports
from utils import Util
from kmeans_clustering import KMeansCluster

# Global definitions
app = Flask(__name__)
api = Api(app)
CORS(app)

# Root
class Root(Resource):
    def get(self):
        filename = './blogdata.txt'
        result = {'message': Util.readfile(filename)}
        return jsonify(result)

# Get the clusters
class Clusters(Resource):
    def get(self, iterations):
        filename = './blogdata.txt'
        data = Util.readfile(filename)

        try:
            number_of_iterations = int(iterations)
        except ValueError:
            number_of_iterations = False
        finally:
            clusters = KMeansCluster.run_assignments(data, 5, number_of_iterations)
            return jsonify([[assignment['blog'] for assignment in cluster.assignments] for cluster in clusters])

# Add resources
api.add_resource(Root, '/') # Route_1
api.add_resource(Clusters, '/clusters/kmeans/<iterations>') # Route_2


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     