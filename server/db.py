from sqlalchemy import create_engine
from flask_jsonpify import jsonify

class DB:
  def __init__(self, dbpath):
    self.db_connect = create_engine('sqlite:///' + dbpath)
    
  def get_ratings_for(self, user_id):
    conn = self.db_connect.connect()
    query = conn.execute("select * from ratings where UserID = " + str(user_id))
    result = [dict(zip(tuple (query.keys()), i)) for i in query.cursor]
    return result

  def get_all_user_ids(self):
    conn = self.db_connect.connect()
    query = conn.execute("select UserID from users")
    result = [i[0] for i in query.cursor.fetchall()]
    return result
  
  def get_name_from_id(self, user_id):
    conn = self.db_connect.connect()
    query = conn.execute("select UserName from users where UserID = " + str(user_id))
    result = [i[0] for i in query.cursor.fetchall()]
    return result