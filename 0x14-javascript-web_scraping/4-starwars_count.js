#!/usr/bin/node
const request = require('request');
const id = 18;
const url = process.argv[2];

request(url, (error, response, body) => {
    if (!error) {
	const res = JSON.parse(body).results;
	const wa = res.filter(movie => movie.characters
		.find(character => character.includes(`/${id}/`)));
	console.log(wa.length);
    }
	if (error) console.log(error);
  }
);
