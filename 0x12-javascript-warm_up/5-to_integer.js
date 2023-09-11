#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2])) === false) {
  const num = Number(argv[2]);
  console.log('My number: ' + num);
} else { console.log('Not a number'); }
