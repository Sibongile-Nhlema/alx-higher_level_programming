#!/bin/bash
# takes in a URL, sends a GET request with a specific header, and displays body
curl -sH "X-School-User-Id: 98" "$1" -X GET
