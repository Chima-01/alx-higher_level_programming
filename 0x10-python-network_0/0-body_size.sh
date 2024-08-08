#!/usr/bin/env bash
# get the content size of a url

if [ "$1" ];
then
	curl -s --head "$1" | grep "Content-Length" | cut -d ' ' -f 2
fi
