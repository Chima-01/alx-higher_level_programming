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
        console.log('C'.repeat(this.size));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
