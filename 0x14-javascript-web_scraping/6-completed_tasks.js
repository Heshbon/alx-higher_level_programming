#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const items = JSON.parse(body);
    for (const a in items) {
      const item = items[a];
      if (item.completed === true) {
        if (completed[item.userId] === undefined) {
          completed[item.userId] = 1;
        } else {
          completed[item.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
