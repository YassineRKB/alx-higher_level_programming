#!/bin/bash
#Bash script to display the size of the body of the response after request to url
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2