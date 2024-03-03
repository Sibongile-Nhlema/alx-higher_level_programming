#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
