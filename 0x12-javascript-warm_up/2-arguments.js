#!/usr/bin/node

const nArgs = process.argv.slice(2).length;
if (nArgs === 0) { console.log('No argument'); } else if (nArgs === 1) { console.log('Argument found'); } else { console.log('Arguments found'); }
