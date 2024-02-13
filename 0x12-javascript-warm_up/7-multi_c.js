#!/usr/bin/node

const argument = process.argv[2];

if (parseInt(argument)) {
	for (let i = 0; i < parseInt(argument); i++) {
		console.log('C is fun');
	}
} else {
  console.log('Missing number of occurrences');
}
