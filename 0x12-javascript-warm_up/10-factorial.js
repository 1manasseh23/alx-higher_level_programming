#!/usr/bin/node

/*
a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
*/

function factorial(x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log("Factorial of NaN is 1");
} else {
  const result = factorial(num);
  console.log(result);
}
