#!/usr/bin/node

const length = process.argv.length - 2;
if (length === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
