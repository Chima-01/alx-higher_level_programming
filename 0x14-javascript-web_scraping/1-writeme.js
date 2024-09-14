#!/usr/bin/node
// A script that writes a string to a file.

const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], function (err) {
  if (err) {
    console.log(err);
  }
});
