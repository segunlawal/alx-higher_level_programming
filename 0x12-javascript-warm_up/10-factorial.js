#!/usr/bin/node

const firstArg = Number(process.argv[2]);
function findFactorial (num) {
  if (isNaN(num)) { return 1; }
  if (num === 0) {
    return 1;
  }
  return num * findFactorial(num - 1);
}
console.log(findFactorial(firstArg));
