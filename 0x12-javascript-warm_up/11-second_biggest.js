#!/usr/bin/node

/* searches the second biggest integer in the list of arguments */

const myArray = process.argv.slice(2, process.argv.length);
let index;

function Max (array) {
  const max = [0, 0];
  let i = 0;
  while (i < array.length) {
    if (array[i] > max[1]) {
      max[1] = array[i];
      max[0] = i;
    }
    i++;
  }

  return (max[0]);
}

if (myArray.length < 2) {
  console.log(0);
} else {
  index = Max(myArray);
  myArray.splice(index, 1);
  index = Max(myArray);
  console.log(myArray[index]);
}
