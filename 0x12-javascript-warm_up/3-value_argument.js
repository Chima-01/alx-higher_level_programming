#!/usr/bin/node
// A script that prints the first argument passed

const argsLength = process.argv.length;

if (argsLength <= 2) {
  console.log('No argument');
} else if (argsLength >= 3) {
  console.log(process.argv[2]);
}
