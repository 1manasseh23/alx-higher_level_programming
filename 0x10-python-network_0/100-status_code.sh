 #!/bin/bash

 # Check if an argument is provided
 if [ $# -ne 1 ]; then
	     echo "Usage: $0 <URL>"
	         exit 1
 fi

 # Function to extract status code using curl
 get_status_code() {
	 # Use curl to send a HEAD request and capture the HTTP status
	 # -s: Silent mode (no progress or error messages)
	 # -o: Write output to /dev/null (we don't care about response body)
	 # -I: Send a HEAD request (headers only)
	 # -w: Custom output format (HTTP status code)
	 # -o /dev/null: Redirects the response body to /dev/null
	 # -w '%{http_code}': Prints the HTTP status code
	 
	 curl -s -o /dev/null -I -w '%{http_code}' "$1"
 }
 
# Call the function to get the status code

status_code=$(get_status_code "$1")

# Display the status code
echo "$status_code"
