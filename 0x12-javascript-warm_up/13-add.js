#!/usr/bin/node
// add two int

function add (a, b) {
  if (Number.isInteger(a) && Number.isInteger(b)) {
    return a + b;
  }
}
module.exports.add = add;
