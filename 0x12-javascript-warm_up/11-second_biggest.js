#!/usr/bin/node
const { argv } = require('process');
if (!argv.length <= 3) {
  const numbers = argv.slice(2);
  numbers.sort(
    (a, b) => b - a
  );
  console.log(numbers[1]);
} else {
  console.log(0);
}
