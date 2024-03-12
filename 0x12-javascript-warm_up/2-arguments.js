#!/usr/bin/node

/*  a script that prints a message depending of the number of arguments passed

const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs === 0)
{
	console.log("No argument");
}
else if (numArgs === 1)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments fund");
}
*/
const argsLength = process.argv.length;

if (argsLength === 2) {
    console.log("No argument");
} else if (argsLength === 3) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
