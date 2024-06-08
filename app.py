from flask import Flask, render_template, redirect, url_for, request, jsonify
from package_creator import create_empty_package  # Import the function
from addToPackage import submit  # Import the submit function

from werkzeug.utils import secure_filename
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


@app.route('/add_to_omp', methods=['POST'])
def add_to_omp():
    try:
        base_url = request.form.get('base_url')
        username = request.form.get('username')
        password = request.form.get('password')
        package_name = request.form.get('package_name')
        file = request.files.get('objects_file')

        # Save the uploaded file to a temporary location
        tmp_dir = '/tmp'
        print(f'Temporary directory: {tmp_dir}')  # Print the location of the /tmp directory
        file_path = os.path.join(tmp_dir, secure_filename(file.filename))
        file.save(file_path)


        # Call the submit function
        submit(base_url, package_name, username, password, file_path)

        return jsonify({'message': 'Objects added to OMP successfully.'}), 200

    except Exception as e:
        logging.error("Error occurred while adding objects to OMP: %s", e)
        return jsonify({'error': 'An error occurred while adding objects to OMP.'}), 500

@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def render_main_page(name=None):
    if name == 'index.html' or name is None:
        return render_template('index.html', name=name)
    else:
        return "Page not found", 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)