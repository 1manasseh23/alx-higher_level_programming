#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
	    echo "Usage: $0 <URL> <filename>"
	        exit 1
fi

# Extract the URL and filename from the arguments
URL="$1"
FILENAME="$2"

# Validate if the file exists
if [ ! -f "$FILENAME" ]; then
	    echo "Error: File '$FILENAME' does not exist."
	        exit 1
fi

# Send the POST request using curl
RESPONSE=$(curl -X POST -H "Content-Type: application/json" -d @"$FILENAME" "$URL")

# Check if the response contains valid JSON
if jq -e . >/dev/null 2>&1 <<< "$RESPONSE"; then
    echo "Valid JSON"
    echo "$RESPONSE"
else
    echo "Not a valid JSON"
fi
