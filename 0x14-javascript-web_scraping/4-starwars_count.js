#!/usr/bin/node
const request = require('request');

request(
  process.argv[2],
  (err, code, body) => {
    if (err) {
      console.error(err);
    } else {
      let totalMovies = 0;
      const data = JSON.parse(body);
      for (const film in data.results) {
        for (const character in data.results[film].characters) {
          if (data.results[film].characters[character].includes('18')) {
            totalMovies += 1;
          }
        }
      }
      console.log(totalMovies);
    }
  });
