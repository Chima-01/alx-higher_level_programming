#!/usr/bin/node
// A script that prints the number of movies
// where the character “Wedge Antilles” is present.

const arg = process.argv[2];
const request = require('request');

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(result => {
      const characters = result.characters;
      const wedgeAntilles = characters.filter(url => {
        const parts = url.split('/');
        return parts[parts.length - 2] === '18';
      });
      count += wedgeAntilles.length;
    });
    console.log(count);
  }
});
