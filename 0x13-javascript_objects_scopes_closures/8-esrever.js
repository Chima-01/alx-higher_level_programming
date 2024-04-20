#!/usr/bin/node
// A Program that reverses a list

exports.esrever = function (list) {
  const reversedArray = [];

  if (!Array.isArray(list)) {
    return;
  }

  for (let i = (list.length - 1); i >= 0; i--) {
    reversedArray.push(list[i]);
  }

  return reversedArray;
};
