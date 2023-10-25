#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
// let num = 0;
// request.get(url, (err, resp) => {
//   if (err) {
//     console.error(err);
//   } else {
//     const all = JSON.parse(resp.body).results;
//     for (const res in all) {
//       if (all[res].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
//         num++;
//       }
//     }
//     console.log(num);
//   }
// });
request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    let counter = 0;
    const { results } = JSON.parse(body.body);

    results.forEach((element, i) => {
      if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        counter++;
      }
    });
    console.log(counter);
  }
});
