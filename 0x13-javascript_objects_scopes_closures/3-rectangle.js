#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const width = this.width;
    const height = this.height;

    for (let i = 0; i < height; i++) {
      console.log('X'.repeat(width));
    }
  }
}

module.exports = Rectangle;
