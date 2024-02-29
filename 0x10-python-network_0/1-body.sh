#!/bin/bash
# script takes URL, sends a GET request, displays body of response for 200 status code
curl -sL "$1" | grep -q "200" && curl -sL "$1"
