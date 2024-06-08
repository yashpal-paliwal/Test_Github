from flask import Flask, render_template, redirect, url_for, request, jsonify
from requests.auth import HTTPBasicAuth
import requests

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        base_url = request.form.get('base_url')
        username = request.form.get('username')
        password = request.form.get('password')
        package_name = request.form.get('package_name')
        package_description = request.form.get('package_description', '')  # Use an empty string if package_description is not provided
        file = request.files.get('file')

        credentials = {
            'base_url': base_url,
            'username': username,
            'password': password,
            'package_name': package_name,
            'package_description': package_description
        }

        return create_empty_package(credentials)
    else:
        return redirect(url_for('render_main_page', name='index.html'))

@app.route('/<name>', methods=['GET'])
def render_main_page(name=None):
    if name == 'index.html':
        return render_template('index.html', name=name)
    else:
        return "Page not found", 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)
