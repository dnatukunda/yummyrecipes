from flask import render_template
from yummyrecipes import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("view.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signupp():
    return render_template("signup.html")