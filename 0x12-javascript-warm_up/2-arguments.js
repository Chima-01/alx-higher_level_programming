#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed

const arg = process.argv;

if (arg.length <= 2) {
  console.log('Arguments found');
} else {
  for (let i = 2; i < arg.length; i++) {
    console.log(arg[i]);
  }
}
