#!/usr/bin/node
exports.addMeMaybe = (num, cb) => {
  const nNum = num + 1;
  cb(nNum);
};
