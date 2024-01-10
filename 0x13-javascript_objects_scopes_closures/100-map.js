#!/usr/bin/node
// A script that imports an array and computes a new array

const list = require('./100-data').list;

const newList = list.map(function (elem, index) {
  return elem * index;
});
console.log(list);
console.log(newList);
