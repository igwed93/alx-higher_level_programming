#!/usr/bin/node

// function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const e of list) {
    if (e === searchElement) {
      occurences += 1;
    }
  }

  return occurences;
};
