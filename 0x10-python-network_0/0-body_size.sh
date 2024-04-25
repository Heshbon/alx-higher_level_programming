#!/bin/bash
# Get the byte size of the HTTP header response for the URL.
curl -sI "$1" | awk '/Content-Length/{print $2}'
