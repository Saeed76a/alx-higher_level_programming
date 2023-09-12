#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0; let time = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      time++;
    }
    i++;
  }
  return time;
};
