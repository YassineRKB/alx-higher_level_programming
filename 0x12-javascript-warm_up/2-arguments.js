#!/usr/bin/node
const argv = import('process');
if (argv.length <= 2) {
  console.log('No argument');
} else if (argv.length <= 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
