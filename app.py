from flask import Flask, jsonify, request
# import pandas as pd
import json

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def hello_world():
    try:
     if(request.method == 'GET'):
        return "Hello World"    


    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })

if __name__ == '__main__':
    app.run(debug=True)