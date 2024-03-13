#!/usr/bin/node

/*
This a class Rectangle that defines a rectangle
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return {};
        } else {
            this.width = w;
            this.height = h;
        }
    }
}
*/
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
