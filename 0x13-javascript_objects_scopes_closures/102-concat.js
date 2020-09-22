#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data1) {
  if (err) {
    return console.log(err);
  }
  fs.readFile(process.argv[3], 'utf8', function (err, data2) {
    if (err) {
      return console.log(err);
    }
    fs.writeFile(process.argv[4], data1 + data2, 'utf8', function (err) {
      return console.log(err);
    });
  });
});
