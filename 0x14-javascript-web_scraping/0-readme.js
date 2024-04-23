#!/usr/bin/env node
/**
 * Reads and prints the content of a file.
 *
 * @param {string} filePath - The file path to read.
 * @throws {Error} If an error occurred during the reading, the error object is thrown.
 */

const fs = require('fs');

function readFile(filePath) {
    // Read the file content in UTF-8 encoding
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// Call the function with the file path as an argument
readFile(process.argv[2]);
