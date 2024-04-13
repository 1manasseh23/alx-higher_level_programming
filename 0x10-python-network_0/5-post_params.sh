#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

URL=$1
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Send a POST request with parameters to the URL and display the response body
curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$URL"
echo ""  # Print a newline after the response bod#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
		fi
		
		URL=$1
		EMAIL="test@gmail.com"
		SUBJECT="I will always be here for PLD"
		
		# Send a POST request with parameters to the URL and display the response body
		curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$URL"
		echo ""  # Print a newline after the response bodyy
