#!/usr/bin/node
const stream = require('fs');

const file = process.argv[2];
stream.readFile(
  file,
  'utf8',
  (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
