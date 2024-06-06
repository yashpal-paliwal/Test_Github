import requests
from requests.auth import HTTPBasicAuth

def create_empty_package():
    # Ask user for environment, package name, description and credentials
    environment = "https://microsoft-dev.iwmsapp.com/tririga" 
    #input("Enter the environment: ")
    package_name = "Test_pipeline_OMP"
    #input("Enter the package name: ")
    package_description = "test-pipeline-omp-description"
    #input("Enter the package description: ")
    username = "ypaliwal"
    #input("Enter your username: ")
    password = "1Password*"
    #input("Enter your password: ")

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
