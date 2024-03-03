#!/usr/bin/python3
'''
takes in url, sends request and
displays value of X-Request_Id variable in header
uses packages requests and sys
'''

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(f"{x_request_id}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
