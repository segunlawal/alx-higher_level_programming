#!/bin/bash
# Sends a request to that URL and displays the size of the body of the response
curl -s -o "$response_file" -w "%{size_download}" "$1"
