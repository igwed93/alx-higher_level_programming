#!/usr/bin/node

/* a script that prints a sqaure
 * */
let size = parseInt(process.argv[2]);
if (process.argv[2] === undefined || !size) {
  console.log('Missing size');
}

let str = '';
for (let i = 0; i < size; i++) {
  str += 'X';
}

while (size > 0) {
  console.log(str);
  size--;
}
