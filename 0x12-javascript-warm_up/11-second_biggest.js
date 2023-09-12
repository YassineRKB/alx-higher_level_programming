#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2);
  numbers.sort(
    (a, b) => b - a
  );
  console.log(numbers[1]);
}
