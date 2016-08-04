from flask import Flask
import requests
import os

dep_endpoint = os.getenv('dep_endpoint');

app = Flask(__name__)

@app.route('/')
def hello():
    msg = requests.get(dep_endpoint);
    return 'Hello ' + msg.text;

if __name__ == '__main__':
        app.run(port=5001,debug=True,host='0.0.0.0')
