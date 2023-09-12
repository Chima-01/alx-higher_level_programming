#!/usr/bin/node
// script that computes and prints a factorial
const num = parseInt(process.argv[2]);
const fact = factorial(num);
console.log(fact);

function factorial (num) {
  if (num <= 0 || !num) {
    return 1;
  }
  return factorial(num - 1) * num;
}
