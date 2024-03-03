#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -s 0.0.0.0:5000/catch_me -X POST -d "user_id=98" -H "Origin: HolbertonSchool"
