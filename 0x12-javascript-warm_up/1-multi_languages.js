#!/usr/bin/node

/* a script that prints 3 lines */

const myCLang = 'C is fun';
const myPython = 'Python is cool';
const myJava = 'JavaScript is amazing';

const myArray = [myCLang, myPython, myJava];
for (const lang in myArray) {
  console.log(myArray[lang]);
}
