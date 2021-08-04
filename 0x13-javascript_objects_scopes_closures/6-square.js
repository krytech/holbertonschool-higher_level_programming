#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = 0; row < this.width; row += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
