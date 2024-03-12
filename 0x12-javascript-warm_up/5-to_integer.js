#!/usr/bin/node

// Check if the first argument can be converted to an integer
function isConvertibleToInteger(arg) {
    return !isNaN(parseInt(arg));
}

function main() {
    const firstArg = process.argv[2];

    if (isConvertibleToInteger(firstArg)) {
        console.log(`My number: ${parseInt(firstArg)}`);
    } else {
        console.log("Not a number");
    }
}
