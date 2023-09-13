#!/usr/bin/node
const list = require('./100-data.js').list;
const nList = list.map((i, index) => i * index);
console.log(list);
console.log(nList);
