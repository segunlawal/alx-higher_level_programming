#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c) {
     for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    } else { super.print(); }
  }
}

module.exports = Square;
