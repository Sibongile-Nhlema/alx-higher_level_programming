#!/bin/bash
# This script sends a JSON POST request to a specified URL with the content of a file as the request body
curl -sX POST "$1" -H "Content-Type: application/json" --data @"$2"
