#!/usr/bin/node
const fs = require('fs');

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

readFile(process.argv[2]);
