#!/usr/bin/node
// A script that prints the addition of 2 integers

const [num1, num2] = [parseInt(process.argv[2]), parseInt(process.argv[3])];

function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
