#!/usr/bin/node
const request = require('request');

request(
  process.argv[2],
  (err, code, body) => {
    if (err) {
      console.error(err);
    } else {
      const data = JSON.parse(body);
      const users = {};
      data.forEach(element => {
        if (element.completed) {
          users[element.userId] = (users[element.userId] || 0) + 1;
        }
      });
      console.log(users);
    }
  });
