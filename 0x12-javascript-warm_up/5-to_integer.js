#!/usr/bin/node

const argument = process.argv[2];

if (parseInt(argument)) {
	console.log('My number: ' + parseInt(argument));
} else {
	console.log('Not a number');
}
