#!/bin/bash
# Take in URL, sends a request to it and displays the status code of the response
curl -sLI -o /dev/null -w "%{http_code}" "$1"
