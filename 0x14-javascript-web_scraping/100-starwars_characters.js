#!/usr/bin/node
/*
* This a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line
* You must use the Star wars API
* You must use the module request
*/
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const charactersUrls = JSON.parse(body).characters;

  charactersUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      console.log(JSON.parse(body).name);
    });
  });
});
