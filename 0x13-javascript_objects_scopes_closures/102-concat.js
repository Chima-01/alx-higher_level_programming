#!/usr/bin/node
// a script that concat two files

const fs = require('node:fs');

const file1 = fs.readFileSync(process.argv[2], 'utf-8');
const file2 = fs.readFileSync(process.argv[3], 'utf-8');
const content = file1 + file2;

fs.writeFileSync(process.argv[4], content);
