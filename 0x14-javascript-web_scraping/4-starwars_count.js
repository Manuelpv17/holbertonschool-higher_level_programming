#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
