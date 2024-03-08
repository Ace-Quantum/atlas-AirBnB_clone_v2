#!/usr/bin/python3

"""
Triple quotes for documentation
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello HBNB'