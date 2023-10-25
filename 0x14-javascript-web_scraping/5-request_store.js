#!/usr/bin/node
const request = require('request');
const stream = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(
  url,
  (err, { body }) => {
    if (err) return console.log(err);
    stream.writeFile(file, body, 'utf8', (err) => {
      err && console.log(err);
    });
  });
