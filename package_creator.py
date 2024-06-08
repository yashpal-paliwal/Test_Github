# package_creator.py
from requests.auth import HTTPBasicAuth
import requests
from flask import jsonify

def create_empty_package(credentials):
    environment = credentials['base_url']
    package_name = credentials['package_name']
    package_description = credentials.get('package_description', '')  # Use an empty string if package_description is not provided
    username = credentials['username']
    password = credentials['password']

    url = f'{environment}/api/p/v1/om/createEmptyPackage?packageName={package_name}&packageDescription={package_description}'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        success_message = f'OMP successfully created at target:  {environment}'
        return jsonify({'message': success_message}), 200
    else:
        return jsonify({'error': f'Request failed with status code {response.status_code}'}), 400
