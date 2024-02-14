#!/usr/bin/node
const dict = require('./101-data').dict;
const userIDsByOccurrence = {};

for (const userID in dict) {
  const occurrence = dict[userID];
  if (occurrence in userIDsByOccurrence) {
    userIDsByOccurrence[occurrence].push(userID);
  } else {
    userIDsByOccurrence[occurrence] = [userID];
  }
}
console.log(userIDsByOccurrence);
