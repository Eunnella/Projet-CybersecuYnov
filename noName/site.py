#!/usr/bin/python3

from re import DEBUG
from flask import Flask, url_for, render_template

app = Flask(__name__)
"""import sqlite3



DATABASE = '/noName/Database.db'
DEBUG = True #Never leave debug mode activated in a production system, because it will allow users to execute code on the server!

app = Flask(__name__)
 app.config.from_object(__name__)

def connection_DB():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db= connection_DB()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close() """

@app.route('/')

def login():
    return render_template("form.html")

if __name__ == '__main__':
    app.run()