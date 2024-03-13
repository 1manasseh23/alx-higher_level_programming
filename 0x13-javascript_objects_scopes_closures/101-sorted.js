#!/usr/bin/node

/*
This is a script that imports a dictionary of occurrences
by user id and computes a dictionary of user ids by occurrence.
*/

const { dict } = require('./101-data');

const usersByOccurrence = {};

for (const userId in dict) {
    const occurrence = dict[userId];
    if (occurrence in usersByOccurrence) {
        usersByOccurrence[occurrence].push(userId);
    } else {
        usersByOccurrence[occurrence] = [userId];
    }
}

console.log(usersByOccurrence);
