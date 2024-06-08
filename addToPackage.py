from requests.auth import HTTPBasicAuth
import pandas as pd
import requests
from flask import jsonify

def submit(base_url, package_name, username, password, file_path):
    # Check if any field is empty
    if not base_url or not package_name or not username or not password:
        return jsonify({'error': 'Please provide all the values.'}), 400
    url = f"{base_url}/api/p/v1/om/addObjectToPackage"
    df = pd.read_excel(file_path, sheet_name='dev_tracker')
    for index, row in df.iterrows():
        params = {
            'packageName': package_name,
            'objectType': row['objectType'],
            'objectName': row['objectName'],
            'moduleName': row['moduleName'],
            'boName': row['boName']
        }
        response = requests.get(url, params=params, auth=HTTPBasicAuth(username, password))

    # Check the status code
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Return a success message
        success_message = f'OMP Objects Added at target:  {base_url}'
        return jsonify({'message': success_message}), 200
        # return jsonify({'message': f"Success: Response Code: {response.status_code}\n{data}"}), 200
    else:
        return jsonify({'error': f'Request failed with status code {response.status_code}'}), 400
