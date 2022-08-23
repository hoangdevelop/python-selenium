from flask import Flask, request
from libs_selenium import screenshot_full_page

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Hello world"

@app.route('/test')
def test():
    url = request.args.get('url')
    screenshot_full_page(url)

    return "take screenshot"

app.run(host='0.0.0.0', port='80')