#!/usr/bin/node
function add (a, b) {
  const res = a + b;
  console.log(res);
}
const { argv } = require('process');
add(argv[2], argv[3]);
