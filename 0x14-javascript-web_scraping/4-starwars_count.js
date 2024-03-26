#!/usr/bin/node

const request = require('request');

function getTotalCharacterPresenceInMovies(apiUrl) {
    const characterId = 18;
    let count = 0;

    function fetchPage(url) {
        request(url, (error, response, body) => {
            if (!error && response.statusCode === 200) {
                const filmsData = JSON.parse(body);
                filmsData.results.forEach(film => {
                    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
                        count++;
                    }
                });
                if (filmsData.next) {
                    fetchPage(filmsData.next);
                } else {
                    console.log(count);
                }
            } else {
                console.error('Error: Unable to fetch movie data');
            }
        });
    }

    fetchPage(apiUrl);
}

const args = process.argv.slice(2);
if (args.length !== 1) {
    console.error("Usage: node <script.js> <api_url>");
    process.exit(1);
}

const apiUrl = args[0];
getTotalCharacterPresenceInMovies(apiUrl);

