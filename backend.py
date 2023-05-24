from flask import Flask, jsonify, request
import scenarios
import view

from flask_cors import CORS
import view
import config
from flask_cors import CORS
import argparse

app = Flask(__name__)
cors = CORS(app)


@app.route('/api/marital_status', methods=['GET','POST'])
def sample1():
    
    
    if request.method == 'GET':
        response = scenarios.marital_status(request.args)
    if request.method == 'POST':
        response = scenarios.marital_status(request.get_json())
    
    return jsonify(response)


@app.route('/api/education', methods=['GET','POST'])
def sample2():
    
    if request.method == 'GET':
        response = scenarios.education(request.args)
    if request.method == 'POST':
        response = scenarios.education(request.get_json())
    
    return jsonify(response)


@app.route('/api/employee', methods=['GET'])
def sample3():
    
    if request.method == 'GET':
        response = scenarios.employee(request.args)
    if request.method == 'POST':
        response = scenarios.employee(request.get_json())
    
    return jsonify(response)

parser = argparse.ArgumentParser(description='Run the application.')


parser.add_argument('--port', type=int, default=5000, help='port number (default: 5000)')
parser.add_argument('--host', type=str, default="127.0.0.1", help='ip address (default: 127.0.0.1)')

args = parser.parse_args()

if __name__ == '__main__':
    view.create_view()
    app.run(debug=True, port=args.port,host=args.host)
