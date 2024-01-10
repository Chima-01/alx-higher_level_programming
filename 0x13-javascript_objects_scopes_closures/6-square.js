#!/usr/bin/node
// square class that inherits from rectangle

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
