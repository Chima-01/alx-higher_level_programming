#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number
// matches a given integer

const param = process.argv[2];
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${param}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
