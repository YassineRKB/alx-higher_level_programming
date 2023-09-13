#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (; i < this.height;) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}
module.exports = Rectangle;
