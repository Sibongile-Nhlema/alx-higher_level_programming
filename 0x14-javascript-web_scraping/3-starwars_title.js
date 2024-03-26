#!/usr/bin/node

const request = require('request');

function getMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Error: Cannot fetch movie title for ID ${movieId}`);
    }
  });
}

const args = process.argv.slice(2);
if (args.length !== 1 || isNaN(args[0])) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
getMovieTitle(movieId);
