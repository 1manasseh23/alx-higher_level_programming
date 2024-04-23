#!/usr/bin/env node
/**
 * Writes a string to a file.
 *
 * @param {string} filePath - The file path to write to.
 * @param {string} stringToWrite - The string to write to the file.
 * @throws {Error} If an error occurred during while writing, the error object is thrown.
 */

const fs = require('fs');

function writeToFile(filePath, stringToWrite) {
  // Write the string to the file in UTF-8 encoding
  fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Successfully written to ${filePath}`);
    }
  });
}

// Call the function with the file path and string to write as arguments
writeToFile(process.argv[2], process.argv[3]);
