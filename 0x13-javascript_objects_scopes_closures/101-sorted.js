#!/usr/bin/node
// creates a new dict with keys correspondig to same value

const dict = require('./101-data').dict;

const keys = Object.values(dict);
const filterKeys = keys.filter(function (ele, idx) {
  return idx === keys.indexOf(ele);
});

const sorted = {};
let temp;

for (let i = 0; i < filterKeys.length; i++) {
  temp = Object.keys(dict).filter(function (ele) {
    return dict[ele] === filterKeys[i];
  });

  sorted[filterKeys[i]] = temp;
  temp = [];
}

console.log(sorted);
