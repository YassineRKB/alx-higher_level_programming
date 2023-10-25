#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url,
  { method: 'GET' },
  (err, { statusCode }) => {
    if (err) return console.log(err);
    console.log(`code: ${statusCode}`);
  });
