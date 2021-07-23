#!/usr/bin/python3

import sqlite3 
from re import DEBUG

from flask import Flask,render_template,request,redirect
from flask.helpers import url_for
from flask_login import login_required, current_user, login_user, logout_user, UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECTRE_KEY'] = 'NewneW'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login = LoginManager()
db = SQLAlchemy(app)
 
class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())
 
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
     
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
 
 
@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))
 
db.init_app(app)
login.init_app(app)

@app.before_first_request
def create_table():
    db.create_all() 


@app.route('/')
def accueil():
    return render_template("accueil.html")


@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method== 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['Password']):
            login_user(user)
            return redirect('/loggedin')
        #does the login process
        #else : 
        return render_template("wrong.html")
    else:
        return render_template("form.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
     
    if request.method == 'POST':
        
        email = request.form['email']
        username = request.form['username']
        password = request.form['Password']
        
        
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/registered')

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
    
    app.run(debug = True)
