#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed

const arg = process.argv;

if (arg.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
