#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const stuff = JSON.parse(body);
    for (let i = 0; i < stuff.length; i++) {
      if (stuff[i].completed === true) {
        if (dict[stuff[i].userId] === undefined) {
          dict[stuff[i].userId] = 1;
        } else {
          dict[stuff[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
