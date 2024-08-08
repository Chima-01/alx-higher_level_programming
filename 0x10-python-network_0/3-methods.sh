#!/bin/bash
# display all http methods server will accept
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f 2-
