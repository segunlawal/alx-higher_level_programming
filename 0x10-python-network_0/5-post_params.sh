#!/bin/bash
# Sends a POST request, and displays the body of the response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
