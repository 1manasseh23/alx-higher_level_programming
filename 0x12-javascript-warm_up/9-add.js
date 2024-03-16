#!/usr/bin/node

/*
This a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
*/

function add(a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log("NaN");
} else {
  const result = add(num1, num2);
  console.log(result);
}

