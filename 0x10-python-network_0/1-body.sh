#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -sL -o "$response_file" -w "%{size_download}" "$1" 
