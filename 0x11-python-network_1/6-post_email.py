#!/usr/bin/python3
'''
takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
uses requests and sys
'''

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to send POST request. Status code: {response.status_code}")
