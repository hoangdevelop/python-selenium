from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port='80')