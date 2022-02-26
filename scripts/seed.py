import json
import sqlite3
import requests
import argparse
from logger_helper import Logging_help
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-t", "--total", type=int, help="Total of records pulled from db")

args = parser.parse_args()
config = vars(args)

log = Logging_help().log

def get_user_attributes(user):
    return {
        'id': user['id'],
        'username': user['login'],
        'avatar_url': user['avatar_url'],
        'type': user['type'],
        'url': user['url']
        }


data=requests.get('https://api.github.com/users').json()

users = list(map(get_user_attributes, data))

if args.total:
  if args.total <= len(users):
    users = users[:args.total]

con = sqlite3.connect('./app/main/database/users.db')

c = con.cursor()

is_table = c.execute(
  """SELECT name FROM sqlite_master WHERE type='table' AND name='Users'; """).fetchall()

if not is_table:
  log.debug('Executing creation of table')
  query = c.execute("""CREATE TABLE Users(
                      id text,
                      username text,
                      avatar_url text,
                      type text,
                      url text
                      )""")


c.executemany("INSERT INTO Users VALUES (:id, :username ,:avatar_url ,:type ,:url )", users)

c.execute("SELECT * FROM Users")

print(c.fetchall())