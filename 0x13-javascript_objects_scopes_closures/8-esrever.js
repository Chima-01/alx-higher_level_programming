#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const reverse = [];
    for (let i = list.length - 1; i >= 0; i--) {
      reverse.push(list[i]);
    }
    return reverse;
  }
};
