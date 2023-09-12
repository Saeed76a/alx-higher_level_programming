#!/usr/bin/node
function f (num) {
  if (num <= 0) {
    return 1;
  }
  return num * f(num - 1);
}

const argc = process.argv.length;
const numb = process.argv[2];
if (argc < 3) {
  console.log(1);
} else {
  console.log(f(Number(numb)));
}
