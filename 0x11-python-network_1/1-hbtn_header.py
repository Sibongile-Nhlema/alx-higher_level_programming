#!/usr/bin/python3
'''Script that takes in a url, sends request it and displays the value of X-Request_Id variable in the header'''


import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
