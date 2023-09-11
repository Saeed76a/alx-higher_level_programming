#!/usr/bin/node

let i = 0; let j; let string = '';
const size = process.argv[2];

if (isNaN(parseInt(size)) || !size) {
  console.log('Missing size');
} else {
  const num = Number(size);
  while (i++ < num) {
    j = 0;
    string = '';
    while (j++ < size) {
      string += 'X';
    }
    console.log(string);
  }
}
