#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(argv[2]);
  let i = 0;
  for (; i < num;) {
    console.log('C is fun');
    i++;
  }
}
