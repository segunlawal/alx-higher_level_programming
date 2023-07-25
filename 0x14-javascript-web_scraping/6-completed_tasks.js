#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const res = JSON.parse(body);
    const tasksCompleted = {};
    res.forEach((todo) => {
      const key = todo.userId;
      if (todo.completed) {
        if (!tasksCompleted[key]) {
          tasksCompleted[key] = 1;
        } else {
          tasksCompleted[key] += 1;
        }
      }
    });
    console.log(tasksCompleted);
  }
  if (error) console.log(error);
}
);
