#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (err, response, body) => {
  if (!err) {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
