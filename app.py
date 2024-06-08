from flask import Flask, render_template, redirect, url_for, request, jsonify
from package_creator import create_empty_package  # Import the function
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
def create_package():
    try:
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
    
    except Exception as e:
        logging.error("Error occurred while creating package: %s", e)
        return jsonify({'error': 'An error occurred while creating the package.'}), 500

@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def render_main_page(name=None):
    if name == 'index.html' or name is None:
        return render_template('index.html', name=name)
    else:
        return "Page not found", 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)