#!/usr/bin/python3
'''Script that takes in aurl, send a request to the URL
   and displays the value of X-Request_Id variable found in the header 
   of the response
'''

import urllib.request
import sys


if len(sys.argv) < 2:
    sys.exit(1)


with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
