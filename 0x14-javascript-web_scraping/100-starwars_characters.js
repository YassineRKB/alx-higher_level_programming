#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (const character of data.characters) {
      request(character, (err, code, body) => {
        const data = JSON.parse(body);
        if (err) {
          console.error(err);
        } else {
          console.log(data.name);
        }
      });
    }
  }
});
