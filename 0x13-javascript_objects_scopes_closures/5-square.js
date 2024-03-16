#!/usr/bin/node

/*
This is a class Square that defines a square and
inherits from Rectangle of 4-rectangle.js

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return;
        }
        this.width = w;
        this.height = h;
    }

    print() {
        if (this.width && this.height) {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }

    rotate() {
        if (this.width && this.height) {
            [this.width, this.height] = [this.height, this.width];
        }
    }

    double() {
        if (this.width && this.height) {
            this.width *= 2;
            this.height *= 2;
        }
    }
}

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
        this.shapeName = 'Square';
    }
}
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }

    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }

    double() {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Square;
