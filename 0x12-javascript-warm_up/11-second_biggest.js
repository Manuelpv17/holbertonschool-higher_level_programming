#!/usr/bin/node

function comp (a, b) {
  return a - b;
}

if (process.argv.length - 2 <= 1) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(comp)[process.argv.length - 4]);
}
