#!/usr/bin/node
const stream = require('fs');

const file = process.argv[1];
const data = process.argv[2];
stream.writeFile(
  file,
  data,
  'utf-8',
  (err) => {
    if (err) console.log(err.message);
  });
