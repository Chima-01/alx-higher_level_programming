#!/usr/bin/node
// A script that computes and prints a factorial

const number = parseInt(process.argv[2]);

function factorial (num) {
  if (!num || num <= 1) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(number));
