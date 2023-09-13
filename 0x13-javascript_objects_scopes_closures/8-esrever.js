#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  while (i < list.length / 2) {
    const swap = list[i];
    list[i] = list[list.length - (i + 1)];
    list[list.length - (i + 1)] = swap;
    i++;
  }
  return list;
};
