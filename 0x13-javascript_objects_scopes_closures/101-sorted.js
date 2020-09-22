#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
Object.keys(dict).forEach(function (key) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
});

console.log(newDict);
