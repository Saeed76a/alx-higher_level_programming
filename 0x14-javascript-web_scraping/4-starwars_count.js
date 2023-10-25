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

request.get(url, (err, resp) => {
  if (err) {
    console.error(err);
  } else {
    console.log(resp.body.split('https://swapi-api.alx-tools.com/api/people/18/').length - 1);
  }
});
