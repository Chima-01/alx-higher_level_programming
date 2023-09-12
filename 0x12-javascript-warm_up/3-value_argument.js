#!/usr/bin/node
// prints the first argument passed to it
const arg = process.argv;

if (arg[2]) {
  console.log(arg[2]);
} else {
  console.log('No argument');
}
