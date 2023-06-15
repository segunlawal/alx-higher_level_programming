#!/usr/bin/node
const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else { super.print(); }
  }
}

module.exports = Square;
