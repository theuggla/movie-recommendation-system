# Server starting point

# Flask imports
from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS

# Local imports
from utils import Util
from kmeans_clustering import KMeansCluster
from hierarchical_clustering import HierchCluster
from print_jpg import Print

# Global definitions
app = Flask(__name__, static_url_path = '/server')
api = Api(app)
CORS(app)

# Root
class Root(Resource):
    def get(self):
        filename = './blogdata.txt'
        result = {'message': Util.readfile(filename)}
        return jsonify(result)

# Get the clusters
class KMeansClusters(Resource):
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

# Get the clusters
class HierchClusters(Resource):
    def get(self):
        filename = './blogdata.txt'
        data = Util.readfile(filename)

        cluster = HierchCluster.cluster(data)
        image_link = Print.draw_dendrogram(cluster, "cluster.jpg")

        return jsonify({'link': "http://localhost:5002/" + image_link})

# Static image host
class ServeStatic(Resource):
    def get(self, path):
        return send_from_directory('img', path)

# Add resources
api.add_resource(Root, '/') # Route_1
api.add_resource(KMeansClusters, '/clusters/kmeans/<iterations>') # Route_2
api.add_resource(HierchClusters, '/clusters/hierarchical') # Route_3
api.add_resource(ServeStatic, '/img/<path>') # Route_4


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     