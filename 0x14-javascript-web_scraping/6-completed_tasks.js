#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
    if (!error) {
	const res = JSON.parse(body);
	const completed = {};
    for (const task of res) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId] += 1;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
    }
	if (error) console.log(error);
  }
);
