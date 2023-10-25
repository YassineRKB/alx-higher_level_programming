#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, { json: true }, (err, filmResponse, filmBody) => {
  if (err) {
    console.error(err);
    return;
  }
  const characterUrls = JSON.parse(filmBody).characters;
  const characterPromises = characterUrls.map(characterUrl => new Promise((resolve, reject) => {
    request(characterUrl, { json: true }, (err, characterResponse, characterBody) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(characterBody).name);
      }
    });
  }));
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(err => {
      console.error(err);
    });
});
