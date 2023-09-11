#!/usr/bin/node
// prints a message depending of the number of arguments passed
const argLength = process.argv.length;

if (argLength === 2) {
  console.log('No argument');
} else if (argLength === 3) {
  console.log('Argument found');
} else if (argLength > 3) {
  console.log('Arguments found');
}
