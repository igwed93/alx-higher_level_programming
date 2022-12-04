#!/usr/bin/node

/* defines a new class that inherits from Rectangle */
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let str = c;
      for (let i = 0; i < this.width; i++) {
        console.log(str.repeat(this.height));
      }
    }
  }
};
