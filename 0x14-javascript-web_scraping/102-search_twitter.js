#!/usr/bin/node

const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const consumer_key = process.argv[2];
const consumer_secret = process.argv[3];

const encodeKey = base64.encode(
  utf8.encode(`${consumer_key}:${consumer_secret}`)
);

request.post(
  {
    url: 'https://api.twitter.com/oauth2/token?grant_type=client_credentials',
    headers: {
      Authorization: `Basic ${encodeKey}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
  },
  function (error, response, body) {
    if (error) {
      console.log(response.statusCode);
    } else {
      const token = JSON.parse(body).access_token;
      request.get(
        {
          url:
            'https://api.twitter.com/1.1/search/tweets.json?q=' +
            process.argv[4] +
            '&count=5',
          headers: { Authorization: 'Bearer ' + token }
        },
        function (error, response, body) {
          if (error) {
            console.log(response.statusCode);
          } else {
            const data = JSON.parse(body).statuses;
            for (let i = 0; i < 5; i++) {
              console.log(
                `[${data[i].id}] ${data[i].text} by ${data[i].user.name}`
              );
            }
          }
        }
      );
    }
  }
);
/*
const urlTweets =
  "https://api.twitter.com/1.1/search/tweets.json?q=" + process.argv[4];
*/
