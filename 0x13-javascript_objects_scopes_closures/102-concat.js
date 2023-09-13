#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');
const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];
const text1 = fs.readFileSync(file1, 'utf8');
const text2 = fs.readFileSync(file2, 'utf8');
const text3 = text1 + text2;
fs.writeFileSync(file3, text3);
