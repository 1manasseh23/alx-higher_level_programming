#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

URL=$1

# Send a DELETE request to the URL and display the response body
curl -X DELETE -s "$URL"
echo ""  # Print a newline after the response body
