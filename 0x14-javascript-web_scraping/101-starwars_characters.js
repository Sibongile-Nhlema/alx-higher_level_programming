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
      const characterPromises = movieData.characters.map((characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, function (charError, charResponse, charBody) {
            if (!charError && charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              resolve(characterData.name);
            } else {
              reject(new Error(`Error fetching character data: ${charError}`));
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then((characterNames) => {
          console.log(characterNames.join('\n'));
        })
        .catch((error) => {
          console.error(error.message);
        });
    }
  });
}

if (movieId) {
  fetchCharacters(movieId);
} else {
  console.error('Usage: node 101-starwars_characters.js <Movie-ID>');
}
