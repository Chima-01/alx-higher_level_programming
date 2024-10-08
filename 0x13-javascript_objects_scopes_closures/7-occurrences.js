#!/usr/bin/node
// A function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count;

  if (!Array.isArray(list) || !searchElement) {
    return;
  }
  count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }

  return count;
};
