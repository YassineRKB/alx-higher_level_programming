#!/bin/bash
#Bash script to display the size of the body of the response after request to url
curl -s $1 | wc -c
