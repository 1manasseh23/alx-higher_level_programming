#!/usr/bin/node

//  a script that prints a message depending of the number of arguments passed

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
