
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = '<h1 style="text-align:center">Hello from Flask' + ' :-)</h1>'
    return msg

