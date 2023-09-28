#!/bin/bash
#Bash script that takes in a URL, displays the size of the body of the response after request
curl -Is "$1" | grep "Content-Length" | cut -d' ' -f2