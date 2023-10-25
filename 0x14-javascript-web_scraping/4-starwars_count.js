#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    let num = 0;
    const { results } = JSON.parse(body.body);

    results.forEach((element, i) => {
      for (const i in element.characters) {
        if (element.characters[i].includes('/18/')) {
          num++;
        }
      }
    });
    console.log(num);
  }
});
