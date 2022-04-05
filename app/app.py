'''demo hello world flask app'''
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''function to return the env message'''
    return f"{os.environ.get('MESSAGE')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug = True, port = "5090")
