#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function fetchCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
    } else if (response && response.statusCode !== 200) {
      console.error('Invalid status code:', response.statusCode);
    } else {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      charactersUrls.forEach(characterUrl => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            console.error('Error:', error);
          } else if (response && response.statusCode !== 200) {
            console.error('Invalid status code:', response.statusCode);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

if (movieId) {
  fetchCharacters(movieId);
} else {
  console.error('Usage: node 100-starwars_characters.js <Movie-ID>');
}
