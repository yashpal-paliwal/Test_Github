function create_empty_package() {
    // Load credentials from json file
    fetch('credentials.json')
        .then(response => response.json())
        .then(credentials => {
            // Get environment, package name, description and credentials from the json file
            const environment = credentials['base_url'];
            const package_name = credentials['package_name'];
            const package_description = "test-pipeline-omp-description";
            const username = credentials['username'];
            const password = credentials['password'];

            // Define the API endpoint
            const url = `${environment}/api/p/v1/om/createEmptyPackage?packageName=${package_name}&packageDescription=${package_description}`;

            // Make a GET request with basic auth
            fetch(url, {
                method: 'GET',
                headers: {
                    'Authorization': 'Basic ' + btoa(username + ":" + password)
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Request failed with status code ' + response.status_code);
                }
            })
            .then(data => {
                // Print the data
                document.getElementById('response').innerText = JSON.stringify(data);
            })
            .catch(error => {
                document.getElementById('response').innerText = error.message;
            });
        });
}
