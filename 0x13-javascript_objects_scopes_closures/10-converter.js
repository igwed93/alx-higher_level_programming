#!/usr/bin/node

// function that converts a number from base 10
// to another base passed as argument

exports.converter = function (base) {
  function converter (number) {
    return number.toString(base);
  }
  return converter;
};
