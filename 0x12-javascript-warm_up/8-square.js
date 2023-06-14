#!/usr/bin/node

const firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) { console.log('Missing size'); }
for (let i = 0; i < firstArg; i++) {
  let row = '';
  for (let j = 0; j < firstArg; j++) {
    row += 'X';
  }
  console.log(row);
}
