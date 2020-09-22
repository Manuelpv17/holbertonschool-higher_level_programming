#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data1) {
  if (err) {
  }
  fs.readFile(process.argv[3], 'utf8', function (err, data2) {
    if (err) {
      // pass
    }
    fs.writeFile(process.argv[4], data1 + data2, 'utf8', function (err) {
      if (err) {
        // pass
      }
    });
  });
});
