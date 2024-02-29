#!/bin/bash
# script takes URL, sends a GET request, displays body of response for 200 status code
curl -sL -w "%{http_code}" -o /dev/null "$1" -X GET && curl -sL "$1"
