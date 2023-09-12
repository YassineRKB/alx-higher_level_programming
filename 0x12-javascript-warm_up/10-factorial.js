#!/usr/bin/node
function getFactor (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * getFactor(num - 1);
}
const { argv } = require('process');
const num = argv[2];
const res = getFactor(num);
console.log(res);
