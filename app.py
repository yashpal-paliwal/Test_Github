from flask import Flask, request, jsonify, render_template
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>', methods=['GET', 'POST'])
def hello(name=None):
    if request.method == 'POST':
        credentials = {
            'base_url': request.form.get('environment'),
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'package_name': request.form.get('package_name')
        }
        if 'file' in request.files:
            file = request.files['file']
            file_credentials = json.load(file)
            for key in file_credentials:
                if file_credentials[key]:  # If the field in the file is not empty, use it
                    credentials[key] = file_credentials[key]
        if not all(credentials.values()):  # Check if any field is left blank
            return jsonify({'error': 'Environment, username, and password cannot be left blank'}), 400
            print('error from app.py hello function')
        return create_empty_package(credentials)
    else: 
        return render_template('index.html', name=name)

def create_empty_package(credentials):
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
        print('error from create_empty_package function')

if __name__ == '__main__':
   app.run(debug=True,port=5001)
