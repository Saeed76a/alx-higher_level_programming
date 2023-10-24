#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, resp) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(resp.body).title);
  }
});
