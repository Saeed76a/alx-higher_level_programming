#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i; let j; let tre = '';
    for (j = 0; j < this.width; j++) {
      tre += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(tre);
    }
  }
}
module.exports = Rectangle;
