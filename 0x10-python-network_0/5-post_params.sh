#!/bin/bash
# takes in a URL, sends a POST request with specific parameters, and displays body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

