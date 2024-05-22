#!/bin/bash
# Sends a request to the URL passed as an argument, and displays the status response of the code.
curl -s -o /dev/null -w "%{http_code}" "$1"
