import json
import sqlite3
import requests
import argparse
from UserModel import User
parser=argparse.ArgumentParser()
parser.add_argument("-t", "--total", type=int, help="Total of records pulled from db")

args = parser.parse_args()
config = vars(args)

con = sqlite3.connect('./app/main/database/users.db')
c = con.cursor()

def get_user_attributes(user):
    return {
        'id': user['id'],
        'username': user['login'],
        'avatar_url': user['avatar_url'],
        'type': user['type'],
        'url': user['url']
        }

def creating_db():
    data=requests.get('https://api.github.com/users').json()

    users = list(map(get_user_attributes, data))

    if args.total:
        if args.total <= len(users):
          users = users[:args.total]



    is_table = c.execute(
      """SELECT name FROM sqlite_master WHERE type='table' AND name='Users'; """).fetchall()

    if not is_table:
        query = c.execute("""CREATE TABLE Users(
                          id text,
                          username text,
                          avatar_url text,
                          type text,
                          url text
                          )""")

    c.executemany("INSERT INTO Users VALUES (:id, :username, :avatar_url, :type, :url )", users)


creating_db()

def get_users(pagination=25):

    c.execute(f"SELECT * FROM Users Limit {pagination}")
    usrs = c.fetchall()
  
    return [User(*u).get_user_dict() for u in usrs]

#c.execute("SELECT * FROM Users")

#sprint(c.fetchall())