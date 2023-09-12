#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const args = process.argv;
const secondBiggest = findSecondBiggest(args);
console.log(secondBiggest);

function findSecondBiggest (args) {
  if (!args || args.length <= 3) {
    return 0;
  }
  const arr = [];
  let biggestNum = parseInt(args[2]);
  let secondBiggest = biggestNum;

  for (let i = 0; i < args.length; i++) {
    arr[i] = parseInt(args[i]);

    if (arr[i] > biggestNum) {
      biggestNum = arr[i];
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > secondBiggest && arr[i] !== biggestNum) {
      secondBiggest = arr[i];
    }
  }
  return secondBiggest;
}
