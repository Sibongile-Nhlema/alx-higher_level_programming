#!/bin/bash
# script takes URL, sends a GET request, displays body of response for 200 status cod
curl -sL -w "%{http_code}" -o /dev/null "$1" -X GET | grep -q "200" && curl -sL "$1"
