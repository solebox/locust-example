from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return "logged in"

@app.route('/profile')
def profile():
    return "coolz"
