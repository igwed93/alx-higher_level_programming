#!/usr/bin/node

// Script that defines a class Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let str = 'X';
    for (let j = 1; j < this.width; j++) {
      str += 'X';
    }

    while (i < this.height) {
      console.log(str);
      i++;
    }
  }
};
