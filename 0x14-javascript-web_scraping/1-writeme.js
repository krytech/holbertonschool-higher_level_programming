#!/usr/bin/node
// Writes a string to a file.
const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, error => {
  if (error) console.log(error);
});
