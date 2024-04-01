#!/usr/bin/env bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a GET request to the URL and store the response in a variable
response=$(curl -s -w "%{http_code}" "$url")

# Extract the HTTP status code from the response
http_code=$(tail -n1 <<< "$response")

# Check if the status code is 200 (OK)
if [ "$http_code" -eq 200 ]; then
    # Remove the last line (status code) from the response
    content=$(sed '$ d' <<< "$response")
    echo "$content"
else
    echo "Error: HTTP status code $http_code"
fi
