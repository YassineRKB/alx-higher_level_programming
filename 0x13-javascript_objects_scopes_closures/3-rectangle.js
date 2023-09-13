#!/usr/bin/node
class Rectangle {
  print () {
    let column = 0;
    for (; col < this.height;) {
      console.log('X'.repeat(this.width));
      column += 1;
    }
  }
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
