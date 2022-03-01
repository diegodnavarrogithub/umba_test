import sqlite3
from flask import Flask
from flask import request
from flask_script import Manager
from flask import render_template
from seed import creating_db, get_users

app = Flask(__name__)
manager = Manager(app)

def build_db():
    creating_db()

@manager.command
def runserver():
    build_db()

@app.route('/')
def index():
    users = get_users()
    return render_template("index.html", title='Users', users=users), 200

@app.route('/users')
def user():
    per_page = request.args.get('pagination')
    users = get_users(int(per_page) if per_page else 25)
    return render_template("index.html", title='Users', users=users), 200    


if __name__ == '__main__':

    app.run()