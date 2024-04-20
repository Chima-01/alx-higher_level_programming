#!/usr/bin/node
// A function that converts a number from base 10 to another
// base passed as argument

exports.converter = function (base) {
  if (!base || base <= 0) {
    return;
  }

  return function (number) {
    return number.toString(base);
  };
};
