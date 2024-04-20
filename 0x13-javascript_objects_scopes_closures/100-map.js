#!/usr/bin/node
// multiplies elements of a list by its index

const list = require('./100-data').list;
console.log(list);
console.log(list.map(function (element) {
  return (element * list.indexOf(element));
})
);
