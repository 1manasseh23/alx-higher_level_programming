#!/usr/bin/node

/* This a script that prints the
 * first argument passed to it
 */

const args = process.argv.slice(2);

if (args[0]) {
  console.log(args[0]);
} else {
  console.log("No argument");
}
