#!/bin/bash
# Script that send a request to a URL passed as an argument, displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
