#!/usr/bin/python3

"""
Triple quotes for documentation
"""

from flask import Flask

app = Flask(__name__)
app.run(host='0.0.0.0', port=5000)

@app.route('/')
def home():
    return 'Hello HBNB'