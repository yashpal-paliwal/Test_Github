import requests
from requests.auth import HTTPBasicAuth
import json

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

        # Print the data
        print(data)
    else:
        print(f'Request failed with status code {response.status_code}')

# Call the function
create_empty_package()
