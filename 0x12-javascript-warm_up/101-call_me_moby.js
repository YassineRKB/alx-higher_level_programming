#!/usr/bin/node
exports.callMeMoby = (x, cb) => {
  let i = 0;
  for (; i < x;) {
    cb();
    i++;
  }
};
