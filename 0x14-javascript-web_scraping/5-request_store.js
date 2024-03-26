#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

function requestAndStore (url, filePath) {
  request(url, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
    } else if (response && response.statusCode !== 200) {
      console.error('Invalid status code:', response.statusCode);
    } else {
      fs.writeFile(filePath, body, { encoding: 'utf-8' }, function (err) {
        if (err) {
          console.error('Error writing to file:', err);
        }
      });
    }
  });
}

if (url && filePath) {
  requestAndStore(url, filePath);
} else {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
}
