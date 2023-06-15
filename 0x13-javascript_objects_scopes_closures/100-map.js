#!/usr/bin/node

const initialList = require('./100-data.js').list;
const newList = initialList.map((item, i) => item * i);
console.log(initialList);
console.log(newList);
