#!/bin/bash
# get the content size of a url
curl -s --head "$1" | grep "Content-Length" | cut -d ' ' -f 2
