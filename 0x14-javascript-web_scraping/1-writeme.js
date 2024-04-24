#!/usr/bin/node

const fs = require('fs');

function writeToFile(filePath, stringToWrite) {
  fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Successfully written to ${filePath}`);
    }
  });
}

writeToFile(process.argv[2], process.argv[3]);
