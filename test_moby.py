# Script for testing the Github class
from github import Github

owner = "moby"
repos = ['moby', 'buildkit', 'tool']
resources = ["issues", "commits", "pulls"]

gh = Github(owner, repos, resources)

# Do while approach
while True:
    data = gh.read()
    if data:
        print(F"Fetched {len(data)} resources")
        # Show information for each resource
        for datum in data:
            print(F"Fetched {len(datum['data'])} {datum['resource']} from {datum['repository']}")
        print('End of read()')
    if data is None:
        break

