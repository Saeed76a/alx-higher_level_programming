#!/usr/bin/node

let numberOfCalls = 0;
exports.logMe = function (item) {
  console.log(numberOfCalls++ + ': ' + item);
};
