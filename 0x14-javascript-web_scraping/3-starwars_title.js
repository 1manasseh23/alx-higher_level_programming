#!/usr/bin/env node
/*
* This a script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
* You must use the module request
*/
const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const movie = JSON.parse(body);
  if (movie.title) {
    console.log(movie.title);
  } else {
    console.error(`Error: No title found for movie with ID ${id}`);
  }
});
