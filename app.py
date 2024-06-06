from flask import Flask, request, jsonify, render_template
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/create_empty_package', methods=['GET'])
def create_empty_package():
    # Load credentials from json file
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)

    # Get environment, package name, description and credentials from the json file
    environment = credentials['base_url']
    package_name = credentials['package_name']
    package_description = "test-pipeline-omp-description"
    username = credentials['username']
    password = credentials['password']

    # Define the API endpoint
    url = f'{environment}/api/p/v1/om/createEmptyPackage?packageName={package_name}&packageDescription={package_description}'

    # Make a GET request with basic auth
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # Check the status code
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({'error': f'Request failed with status code {response.status_code}'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)