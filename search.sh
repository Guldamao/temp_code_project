#!/bin/bash

# Initialize variables with default values
search_path="/"
file_name=""
output_file="$(dirname "$0")/found.txt"

# Parse command line options
while getopts ":p:n:" opt; do
  case $opt in
    p)
      search_path="$OPTARG"
      ;;
    n)
      file_name="$OPTARG"
      ;;
    \?)
      echo "Usage: $0 -p <path> -n <filename>"
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument."
      exit 1
      ;;
  esac
done

# Check if file name is provided
if [ -z "$file_name" ]; then
  echo "Please provide a file name with -n."
  exit 1
fi

# Perform the search using 'find' command, redirecting stderr to /dev/null
find "$search_path" -iname "$file_name" > "$output_file" 2> /dev/null

echo "Search results saved to '$output_file'"

