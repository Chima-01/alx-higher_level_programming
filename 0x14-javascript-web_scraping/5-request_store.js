#!/usr/bin/node
// A  script that gets the contents of a webpage
// and stores it in a file.

const args = process.argv;
const fs = require('fs');
const request = require('request');

request(args[2]).pipe(fs.createWriteStream(args[3]));
