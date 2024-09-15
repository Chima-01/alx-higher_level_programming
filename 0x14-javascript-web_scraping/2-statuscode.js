#!/usr/bin/node
// A script that display the status code of a GET request

const args = process.argv;
const request = require('request');

request.get(args[2]).on('response', function (response) {
  console.log('code:', response && response.statusCode);
});
