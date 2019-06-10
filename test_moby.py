# Script for testing the Github class
import time
from github import Github

owner = "moby"
repos = ['moby', 'buildkit', 'tool']
resources = ["issues", "commits", "pulls"]

gh = Github(owner, repos, resources)

# Do while approach
while True:
    data = gh.read()
    if data:
        print('Fetched {} resources'.format(len(data)))
        # Show information for each resource
        for datum in data:
            print('Fetched {} {} from {}'.format(
                len(datum['data']),
                datum['resource'],
                datum['repository']
            ))
            time.sleep(5)
        print('End of read()')
    if data is None:
        break

