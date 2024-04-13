#!/bin/bash

# Check if the user provided a URL
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

url="$1"

# Send an OPTIONS request using curl
response=$(curl -i -L -X OPTIONS "$url" 2>/dev/null)

# Extract the Allow header from the response
allowed_methods=$(echo "$response" | grep -i "^Allow:" | cut -d' ' -f2-)

# Display the supported methods
echo "Supported HTTP methods for $url: $allowed_methods"
