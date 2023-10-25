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
      for (const element in data) {
        if (data[element].completed) {
          users[data[element].userId] = (users[data[element].userId] || 0) + 1;
        }
      }
      console.log(users);
    }
  });
