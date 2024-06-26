#!/usr/bin/node
/*
* This a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
*/
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
