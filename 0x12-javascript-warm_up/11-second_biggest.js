#!/usr/bin/node
// A script that searches the second biggest integer
// in the list of arguments

const args = process.argv;

function secondLargestNum (args) {
  let largest, secondLargest;

  if (args.length <= 3) {
    return 0;
  }
  largest = parseInt(args[2]);
  secondLargest = largest;

  for (let i = 2; i < args.length; i++) {
    const temp = parseInt(args[i]);
    if (temp > largest) {
      largest = temp;
    }
  }

  for (let i = 2; i < args.length; i++) {
    const temp = parseInt(args[i]);
    if (temp > secondLargest && temp < largest) {
      secondLargest = temp;
    }
  }
  return secondLargest;
}

console.log(secondLargestNum(args));
