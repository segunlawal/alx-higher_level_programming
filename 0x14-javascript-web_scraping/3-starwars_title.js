#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(
  { url, encoding: 'utf-8' },
  (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).title);
    }
  }
);
