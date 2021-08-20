#!/bin/bash
# sends a request to a url and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
