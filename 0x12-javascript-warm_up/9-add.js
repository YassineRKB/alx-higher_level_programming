#!/usr/bin/node
function add (a, b) {
  return Number(a) + Number(b);
}
const { argv } = require('process');
const res = add(argv[2], argv[3]);
console.log(res);
