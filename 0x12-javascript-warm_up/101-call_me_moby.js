#!/usr/bin/node

// This a function that executes x times a function.

const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports = { callMeMoby };
