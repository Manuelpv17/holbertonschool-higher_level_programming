#!/usr/bin/node

const request = require('request');
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlMovie, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      request(film.characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const actor = JSON.parse(body);
          console.log(actor.name);
        }
      });
    }
  }
});
