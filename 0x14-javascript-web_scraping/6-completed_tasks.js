#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const obj = {};
request.get(url, (err, resp) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(resp.body);
    for (const i in tasks) {
      const key = tasks[i].userId.toString();
      if (key in obj) {
        obj[key] = tasks[i].completed ? obj[key] + 1 : obj[key];
      } else if (tasks[i].completed) {
        obj[key] = 1;
      }
    }
    console.log(obj);
  }
});
