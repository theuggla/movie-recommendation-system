# Class to communicate with the database

# External imports
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

class DB:
  
  # Initiates connection to the given database through sqlite
  def __init__(self, dbpath):
    self.db_connect = create_engine('sqlite:///' + dbpath)

  # Returns the ratings for a given user  
  def get_ratings_for(self, user_id):
    conn = self.db_connect.connect()
    query = conn.execute("select * from ratings where UserID = " + str(user_id))
    result = [dict(zip(tuple (query.keys()), i)) for i in query.cursor]
    return result

  # Returns all users
  def get_all_users(self):
    conn = self.db_connect.connect()
    query = conn.execute("select * from users")
    result = [dict(zip(tuple (query.keys()), i)) for i in query.cursor]
    return result

  # Returns all user ids
  def get_all_user_ids(self):
    conn = self.db_connect.connect()
    query = conn.execute("select UserID from users")
    result = [i[0] for i in query.cursor.fetchall()]
    return result
  
  # Returns the username for the given id
  def get_name_from_id(self, user_id):
    conn = self.db_connect.connect()
    query = conn.execute("select UserName from users where UserID = " + str(user_id))
    result = [i[0] for i in query.cursor.fetchall()]
    return result