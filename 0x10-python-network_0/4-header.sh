#!/bin/bash
# Sends a GET request with  header, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1" 
