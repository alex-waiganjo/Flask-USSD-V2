import base64
from datetime import datetime
from flask import Flask, request, jsonify
import requests
import random
import string


app = Flask(__name__)

 # Index Route
@app.route('/', methods=['POST','GET'])
def index():
    return {"Message":"API is working"}


# Dashboard Route
@app.route('/dashbaord', methods=['POST','GET'])
def dashboard():
    return {"Message":"Dashboard is working"}

if __name__ == '__main__':
    app.run(debug=True)
