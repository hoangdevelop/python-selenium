from flask import Flask
import selenium

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Hello world"

@app.route('/screenshot')
def index():
    return screenshot();

app.run(host='0.0.0.0', port='5001')