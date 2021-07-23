#!/usr/bin/python3

import sqlite3, os 
from re import DEBUG

from flask import Flask, jsonify, render_template, request, g, redirect
from flask.helpers import url_for



app = Flask(__name__)
app.database = "Database.db"
DATABASE = 'Database.db'


@app.route('/')
def accueil():
    return render_template("accueil.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password =request.form['Password']
        g.db = sqlite3.connect(DATABASE)
        cur = g.db.execute("SELECT * FROM users WHERE username = '%s' AND password_hash = '%s'" %(username, password))
        if cur.fetchone():
            result = {'status': 'success'}
        else:
            result = {'status': 'fail'}
        g.db.close()
        return jsonify(result)

    return render_template("formvulne.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('registration.html')

@app.route('/registered')
def registered():
    return render_template("registered.html")
    
@app.route('/loggedin')
def loggedin():
    return render_template("loggedin.html")

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == '__main__':
    
    app.run(debug = True)# ne pas laisser le DEBUG sur True !!!!
