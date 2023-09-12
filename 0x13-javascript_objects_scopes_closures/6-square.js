#!/usr/bin/node

const dadSquare = require('./5-square');

class Square extends dadSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i; let j; let tre = '';
      for (j = 0; j < this.width; j++) {
        tre += c;
      }
      for (i = 0; i < this.height; i++) {
        console.log(tre);
      }
    }
  }
}

module.exports = Square;
