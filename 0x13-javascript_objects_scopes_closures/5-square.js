#!/usr/bin/node

/* defines a new class that inherits from Rectangle */
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size); // call the super class constructor and pass in the size parameter
  }
};
