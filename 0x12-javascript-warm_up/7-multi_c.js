#!/usr/bin/node

/* a script that prints 3 lines */
let count = parseInt(process.argv[2]);
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
while (count > 0) {
  console.log('C is fun');
  count--;
}
