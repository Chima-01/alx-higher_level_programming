#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number
// matches a given integer

const arg = process.argv[2];
const request = require('request');

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTask = {};
    const results = JSON.parse(body);

    for (let i = 0; i < results.length; i++) {
      let taskComplete = 0;
      const userId = results[i].userId;
      for (let j = 0; j < results.length; j++) {
        if (results[j].userId === userId) {
          if (results[j].completed) { taskComplete++; }
        }
      }
      if (taskComplete !== 0) { completedTask[userId] = taskComplete; }
    }
    console.log(completedTask);
  }
});
