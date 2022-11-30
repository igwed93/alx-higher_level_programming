#!/usr/bin/node

/*
 script that prints a message depending on
 the number of arguments passed
 */

// assign argv to a variable
const args = process.argv;

// print commandline arguments
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
