#!/usr/bin/node

const request = require('request');

function totalCharacterPresenceInMovie (apiUrl) {
  const characterId = 18;
  let count = 0;

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmsData = JSON.parse(body).results;
      filmsData.forEach(film => {
        if (film.characters.find(character => character.endsWith(`/${characterId}/`))) {
          count++;
        }
      });
      console.log(count);
    } else {
      console.error('Error: Cannot to fetch movie data');
    }
  });
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = args[0];
totalCharacterPresenceInMovie(apiUrl);
