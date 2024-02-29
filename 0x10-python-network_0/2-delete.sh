#!/bin/bash
# sends DELETE request to URL passed as irst argument, displays body ofresponse
curl -sL -w "%{http_code}" "$1" -X DELETE
