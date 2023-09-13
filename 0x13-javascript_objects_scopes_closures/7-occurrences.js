#!/usr/bin/node
const nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const element of list) {
    if (element === searchElement) {
      c++;
    }
  }
  return c;
};
module.exports = nbOccurences;
