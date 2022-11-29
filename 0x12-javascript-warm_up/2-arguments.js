#!/usr/bin/node

/*
 script that prints a message depending on
 the number of arguments passed
 */

// assign argv to a variable
const args = process.argv;

if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
