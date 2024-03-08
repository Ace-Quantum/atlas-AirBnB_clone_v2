#!/usr/bin/python3

"""
Triple quotes for documentation
"""

from flask import Flask

"""
More documentation because idk where they want it
"""

app = Flask(__name__)
app.run(host='0.0.0.0', port=5000)

"""
Documentation here?
"""

@app.route('/')
def home():
    return 'Hello HBNB!'