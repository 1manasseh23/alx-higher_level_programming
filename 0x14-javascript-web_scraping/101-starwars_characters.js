#!/usr/bin/node
/*
* This a script that prints all characters of a Star Wars movie:
*  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line in the same order of the list “characters” in the /films/ response
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
  let characterIndex = 0;

  const printCharacter = () => {
    if (characterIndex >= charactersUrls.length) {
      return;
    }

    request(charactersUrls[characterIndex], (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      console.log(JSON.parse(body).name);
      characterIndex++;
      printCharacter();
    });
  };

  printCharacter();
});
