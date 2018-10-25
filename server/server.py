from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///db/movies.db')
app = Flask(__name__)
api = Api(app)



class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from users")
        return {'users': [i[0] for i in query.cursor.fetchall()]}ID

class Ratings(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from ratings;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Users_Name(Resource):
    def get(self, user_id):
        conn = db_connect.connect()
        query = conn.execute("select * from users where UserId =%d "  %int(user_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Users, '/users') # Route_1
api.add_resource(Ratings, '/ratings') # Route_2
api.add_resource(Users_Name, '/users/<user_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
     