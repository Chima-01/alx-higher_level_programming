#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);
const secondBiggest = findSecondBiggest(args);
console.log(secondBiggest);

function findSecondBiggest (args) {
  if (!args || args.length <= 1) {
    return 0;
  }

  const arr = [];
  let biggestNum = parseInt(args[0]);
  let secondBiggest = biggestNum;

  for (let i = 0; i < args.length; i++) {
    arr[i] = parseInt(args[i]);

    if (arr[i] > biggestNum) {
      biggestNum = arr[i];
    }
  }

  if (arr.length === 2) {
    if (arr[0] > arr[1]) {
      return arr[1];
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > secondBiggest && arr[i] !== biggestNum) {
      secondBiggest = arr[i];
    }
  }
  return secondBiggest;
}
