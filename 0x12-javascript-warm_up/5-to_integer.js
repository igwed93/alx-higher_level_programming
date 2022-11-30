#!/usr/bin/node

/*
script that prints My number: <first argument converted in integer>
*/

const myNum = process.argv[2];

if (parseInt(myNum)) {
  console.log(`My number: ${parseInt(myNum)}`);
} else {
  console.log('Not a number');
}
