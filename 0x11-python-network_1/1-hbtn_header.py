#!/usr/bin/python3
'''takes in url, sends request and displays value of X-Request_Id variable in header'''

import urllib.request
import sys


if len(sys.argv) < 2:
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
except Exception as e:
    print(f"Error occurred: {e}")
