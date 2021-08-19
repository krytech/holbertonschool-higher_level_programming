#!/bin/bash
# displays all HTTP methods that a server will accept given a url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
