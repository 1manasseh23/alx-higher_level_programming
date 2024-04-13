#!/bin/bash

# Send a request to the specified URL
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "$1"
