#!/usr/bin/node

const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const consumerKey = process.argv[2];
const consumerSecret = process.argv[3];

const encodeKey = base64.encode(
  utf8.encode(`${consumerKey}:${consumerSecret}`)
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
    if (!error) {
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
          if (!error) {
            const data = JSON.parse(body).statuses;
            if (data) {
              for (let i = 0; i < data.length; i++) {
                console.log(
                  `[${data[i].id}] ${data[i].text} by ${data[i].user.name}`
                );
              }
            }
          }
        }
      );
    }
  }
);
