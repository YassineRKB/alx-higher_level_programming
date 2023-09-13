#!/usr/bin/node
const SquareOrigin = require('./5-square');

class Square extends SquareOrigin {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
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
