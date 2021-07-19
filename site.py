#!/usr/bin/python3

from re import DEBUG
import sqlite3
from flask import Flask, request, url_for, render_template


DATABASE = '/noName/Database.db'
DEBUG = True #Never leave debug mode activated in a production system, because it will allow users to execute code on the server!

app = Flask(__name__)
app.config.from_object(__name__)

def connection_DB():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')

def first_site():
    return 'congrats !'

if __name__ == '__main__':
    app.run()