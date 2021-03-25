from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/app')
def application():
    return render_template('index.html')