#!/bin/bash
# Script to displays only the status code of the response.
curl -so /dev/null/ -w "%{http_code}" "$1"
