#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);
  let i = 0;
  const line = '#' * num;
  for (; i < num;) {
    console.log(line);
    i++;
  }
}
