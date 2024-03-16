#!/usr/bin/node

/*
This a class Square that defines a square and inherits
from Square of 5-square.js
*/

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
    charPrint(c = 'X') {
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Square;
