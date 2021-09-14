#!/usr/bin/node
// Prints the title of the Star Wars movie corresponding to the given integer.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
