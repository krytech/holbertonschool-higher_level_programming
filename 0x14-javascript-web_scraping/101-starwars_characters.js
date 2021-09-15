#!/usr/bin/node
// Prints all characters in order from a Star Wars movie.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    orderedCharacters(characters, 0);
  }
});
function orderedCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        orderedCharacters(characters, index + 1);
      }
    }
  });
}
