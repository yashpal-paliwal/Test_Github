import pandas as pd
import requests
import json
import glob
from requests.auth import HTTPBasicAuth

# Load credentials from json file
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

base_url = credentials['base_url']
username = credentials['username']
password = credentials['password']
package_name = credentials['package_name']  # Add this line

# Find the excel file with 'development_tracker' in its name
file_path = next(glob.iglob('*development_tracker*.xlsx'), None)
if not file_path:
    print("Error: No file found with 'development_tracker' in its name.")
    exit(1)

def submit():
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
        print(response.json())

    # Check the status code
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Print the data
        print(f"Success: Response Code: {response.status_code}\n{data}")
    else:
        print(f"Error: Request failed with status code {response.status_code}")

submit()