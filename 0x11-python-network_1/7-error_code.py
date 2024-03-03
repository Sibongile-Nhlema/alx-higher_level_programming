#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
Uses requests and sys imports only.
'''

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
