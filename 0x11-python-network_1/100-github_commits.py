#!/usr/bin/python3
'''
Interview questions for a back-end position
'''

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits_data = response.json()
        for commit in commits_data:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Error fetching data from GitHub API")
