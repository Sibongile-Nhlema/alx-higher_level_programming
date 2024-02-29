#!/bin/bash
# sends DELETE request to URL passed as irst argument, displays body ofresponse
curl -s "$1" -X DELETE
