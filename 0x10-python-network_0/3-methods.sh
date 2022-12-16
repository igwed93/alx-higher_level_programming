#!/bin/bash
# Takes in URL and displays all HTTP methods the server will accept
curl -siXL OPTIONS "$1"
