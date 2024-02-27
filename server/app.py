#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h2> Hello World! </h2>'

@app.route('/<string:username>')
def index(username):
    return f'<h2> Welcome to flask {username}! </h2>'

if __name__ == '__main__':
    app.run(port=5555)
