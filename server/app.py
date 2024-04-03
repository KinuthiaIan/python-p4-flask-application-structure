#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Routing views using the @app.route decorator
@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

# Variable Routes
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Running the Flask Development server using the app.run() method
if __name__ == '__main__':
    app.run(port=5555)
