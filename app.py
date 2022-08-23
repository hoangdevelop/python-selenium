from flask import Flask
import libs_selenium

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Hello world"

@app.route('/screenshot')
def screenshot():
    return screenshot();

app.run(host='0.0.0.0', port='5001')