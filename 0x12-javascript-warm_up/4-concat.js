#!/usr/bin/node

/* This a script that prints two arguments passed to it, in
 * the following format: “ is ”
 */

const args = process.argv.slice(2);

if (args[0] && args[1]) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log("No argument provided");
}
