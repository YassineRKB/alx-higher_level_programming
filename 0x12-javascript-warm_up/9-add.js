#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  const res = a + b;
  console.log(res);
}
add(argv[2], argv[3]);
