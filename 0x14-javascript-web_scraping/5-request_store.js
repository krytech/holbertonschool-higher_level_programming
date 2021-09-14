#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
