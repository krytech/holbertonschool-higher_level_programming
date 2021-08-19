#!/bin/bash
# gets the byte size of the HTTP response header from a given url
curl -s "$1" | wc -c
