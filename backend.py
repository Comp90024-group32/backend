from flask import Flask, jsonify, request
import scenarios
import view

from flask_cors import CORS

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

"""
@app.route('/api/sample4', methods=['GET'])
def sample4():
    
    
    
    response = scenarios.sample4(request.args)
    
    return jsonify(response)


@app.route('/api/sample5', methods=['GET'])
def sample5():
    
    
    
    response = scenarios.sample5(request.args)
    
    return jsonify(response)
"""
if __name__ == '__main__':
    view.create_view()
    app.run(debug=True)
    