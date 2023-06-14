#!/usr/bin/node

const firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) { console.log('Missing number of occurrences'); }
for (let i = 0; i < firstArg; i++) {
  console.log('C is fun');
}
