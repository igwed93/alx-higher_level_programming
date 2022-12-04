#!/usr/bin/node

// function that prints the number of arguments
// already printed and the new argument value

let count = -1;
exports.logMe = function (item) {
  count++;
  console.log(`${count}: ${item}`);
};
