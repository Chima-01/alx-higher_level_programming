#!/usr/bin/node
// Returns the number of times a functions has been called

let count = 0;

exports.logMe = function (item) {
  if (!item) {
    return;
  }

  console.log(`${count}: ${item}`);
  count += 1;
};
