#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

URL=$1

# Send a GET request with custom header to the URL and display the response body
curl -s -H "X-School-User-Id: 98" "$URL"
echo ""  # Print a newline after the response body1:ew

