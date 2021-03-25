from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/app')
def app():
    return render_template('index.html')