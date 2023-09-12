#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);
  let i = 0;
  let j = 0;
  for (; i < num;) {
    i++;
	for (; j < num;) {
	  console.log(line);
	  j++;
	}
  }
}
