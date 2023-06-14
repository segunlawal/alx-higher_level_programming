#!/usr/bin/node

const argArr = process.argv;
const firstArg = Number(argArr[2]);
const newArr = argArr.slice(2).sort((a, b) => b - a);
if (!firstArg || argArr.length === 3) { console.log(0); } else { console.log(newArr[1]); }
