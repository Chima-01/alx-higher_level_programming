#!/usr/bin/node
// Write a script that prints x times “C is fun”
const X = parseInt(process.argv[2]);
if (X) {
  for (let i = 0; i < X; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
