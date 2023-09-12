#!/usr/bin/node
exports.addMeMaybe = (num, cb) => {
  const nNum = num++;
  cb(nNum);
};
