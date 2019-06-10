# Streaming Data Excercise


## Description
A small library that can ingest unlimited data from Github.

## Details

This library implement a single class, called GitHub. the class constructor​ is initiated using three variables which are as follows:
- owner - A string representing the Owner​ name
- repo - A list of strings representing Repository​ names
- resources - A list of desired resource names
    - Supported resources: commits, issues, pulls, contributors, languages, teams, tags


The read() function reqturns a portion of data (list of dictionaries composed of Github API data points) everytime it is ran.

## Testing the library
1. Clone or download the repository
2. Rename .env.sample into .env
3. Add your Github username and [personal access token(https://help.github.com/en/enterprise/2.16/user/articles/creating-a-personal-access-token-for-the-command-line)

#### Run the following on shell while in the folder directory
4. pip install -r requirements.txt
5. python test_moby.py
