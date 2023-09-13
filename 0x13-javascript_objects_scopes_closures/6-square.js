#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPoint (c) {
    if (!c) {
      c = 'X';
    }
    let i = 0;
    for (; i < this.height;) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;
