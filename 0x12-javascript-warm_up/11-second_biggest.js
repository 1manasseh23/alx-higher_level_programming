#!/usr/bin/node

/*
This a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
*/

function findSecondLargestInteger(...numbers) {
  if (numbers.length < 2) {
    console.log(0);
    return;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = parseInt(numbers[i]);

    if (isNaN(currentNumber)) {
      console.log("NaN");
      return;
    }

    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber < largest) {
      secondLargest = currentNumber;
    }
  }

  console.log(secondLargest);
}

findSecondLargestInteger(4, 2, 5, 3, 0, -3);
