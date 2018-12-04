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

# Definitions
app = Flask(__name__, static_url_path = '/server')
api = Api(app)

root_url = 'http://localhost:5002/'

programming_articles_directory = './data/Programming'
games_articles_directory = './data/Games'

initialWordList = ['language', 'programming', 'computer', 'software', 'hardware', 'data', 'player', 'online', 'system', 'development',
'machine', 'console', 'developer', 'design', 'history', 'technology', 'standard', 'information', 'article', 'example']
generatedWordList = Util.generate_word_list({'gaming': games_articles_directory, 'programming': programming_articles_directory})

# Setup
CORS(app)

Util.createfile('initial_word_list.txt', initialWordList, programming_articles_directory, True)
Util.createfile('initial_word_list.txt', initialWordList, games_articles_directory, False)

Util.createfile('generated_word_list.txt', generatedWordList, programming_articles_directory, True)
Util.createfile('generated_word_list.txt', generatedWordList, games_articles_directory, False)

# Get the clusters
class Clusters(Resource):
    def get(self, word_list_selection, iterations = None):
        filename = './' + word_list_selection + '_word_list.txt'
        data = Util.readfile(filename)

        if iterations is None:
            cluster = HierchCluster.cluster(data)
            image_link = Print.draw_dendrogram(cluster, word_list_selection + '_wl_cluster.jpg')
            return jsonify(root_url + image_link)
        else:
            try:
                number_of_iterations = int(iterations)
            except ValueError:
                number_of_iterations = False
            finally:
                clusters = KMeansCluster.run_assignments(data, 2, number_of_iterations)
                return jsonify([[assignment['blog'] for assignment in cluster.assignments] for cluster in clusters])


# Static image host
class ServeStatic(Resource):
    def get(self, path):
        return send_from_directory('img', path)

# Add resources
api.add_resource(Clusters, '/clusters/<word_list_selection>/<iterations>', '/clusters/<word_list_selection>/') # Route_1
api.add_resource(ServeStatic, '/img/<path>') # Route_2


# Start server
if __name__ == '__main__':
     app.run(port='5002')
     