#!/usr/bin/node

// function that returns the reversed version of a list

exports.esrever = function (list) {
  const myList = [];
  let length = list.length - 1;
  while (length >= 0) {
    myList.push(list[length]);
    length--;
  }

  return myList;
};
