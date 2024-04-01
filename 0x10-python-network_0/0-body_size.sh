#!/usr/bin/env bash
# Check if URL rgument is provided

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and store the body size in bytes
body_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}')

# Display the body size
echo "$body_size"
