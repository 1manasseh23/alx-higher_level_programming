#!/usr/bin/env node
/*
* This a script that prints the number of movies where the character “Wedge Antilles” is present.

* The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
*  Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
* You must use the module request
*/
const request = require('request');
const url = process.argv[2];
const characterId = 18;

let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const films = JSON.parse(body).results;

  films.forEach((film) => {
    request(film.url, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      const charactersUrls = JSON.parse(body).characters;

      charactersUrls.forEach((characterUrl) => {
        const characterNumber = characterUrl.split('/').filter(Boolean).pop();
        if (characterNumber === `${characterId}`) {
          count++;
        }
      });

      if (films.indexOf(film) === films.length - 1) {
        console.log(count);
      }
    });
  });
});
