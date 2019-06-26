import os
import requests
from dotenv import load_dotenv

# Loads the environment variables from .env
load_dotenv()

class Github:

    # Declare base API URL for easier modification
    BASE_URL = 'https://api.github.com'

    # Number of data returned per page
    MAX_RESULTS = 25

    # Authentication - required to bypass the rate limiting of Github API
    USER = os.environ['GITHUB_USER']
    TOKEN = os.environ['GITHUB_TOKEN']

    def __init__(self, owner, repositories, resources):
        # Instantiating the 3 required input variables
        self.owner = owner
        self.repositories = repositories
        self.resources = resources

        # Create a list of endpoint per each repository/resource.
        # This will serve as the storage of the pagination URL for Github API endpoint
        self.endpoints = []

        # Temporarily assigning an index to the endpoint as a workaround
        index = 0 
        
        for repository in self.repositories:
            for resource in self.resources:
                self.endpoints.append({
                    'index': index,
                    'repository' : repository,
                    'resource': resource,
                    'next_page_url': "",
                    'depleted': False
                })
                index += 1

    # Private function responsible for sending the GET request via requests library
    # This function accepts one parameter (endpoint) and also updates self.endpoints to store the Github API pagination URL
    def __get_resource(self, endpoint):

        # Set the request URL with respect to Github API pagination
        if endpoint['next_page_url']:
            url = endpoint['next_page_url']
        else:
            url = F"{self.BASE_URL}/repos/{self.owner}/{endpoint['repository']}/{endpoint['resource']}"

        # Set request parameters and authentication headers
        params = {'per_page' : self.MAX_RESULTS }
        headers = {'Authorization': F"token {self.TOKEN}"}
        
        # Send the GET request
        response = requests.get(url, params, headers=headers)

        # Check for response status code and assign the next_page_url from Github API to the self.resource object
        if response.status_code == 200:
            # Store the next_page_url for the Github API endpoint if 'next' is available in the response headers
            if 'next' in response.links.keys():
                self.endpoints[endpoint['index']]['next_page_url'] = response.links['next']['url']

            # Mark the resource as depleted if 'next' is not in the response headers            
            else:
                self.endpoints[endpoint['index']]['next_page_url'] = None
                self.endpoints[endpoint['index']]['depleted'] = True                
            
            # return the API endpoint response in JSON format
            return response.json()

        else:
            return False


    # The main function, each call to this function returns the data points for each of the resources
    def read(self):
        data = list()
        for endpoint in self.endpoints:
            # Call the get_resource function by providing the required parameters
            if not endpoint['depleted']:
                result = self.__get_resource(endpoint)

                # If result is not empty add the result to the data list
                if result:
                    data.append({
                        'repository': endpoint['repository'],
                        'resource': endpoint['resource'],
                        'data': result
                    })

        # Return data if not empty
        if data:
            return data
        # Else return NoneType, ending the iteration
        else:
            return None
