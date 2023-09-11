#!/usr/bin/node
const argv = require('process');
if (argv.lenght === 2) {
  console.log('No arguments');
} else if (argv.lenght === 3) {
  console.log('Argument found');
} else {
  console.log('arguments found');
}
