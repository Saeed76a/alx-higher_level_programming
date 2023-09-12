#!/usr/bin/node

module.exports = {
  callMeMoby: function (x, theFunction) {
    let t = 0;
    while (t < x) {
      theFunction();
      t++;
    }
  }
};
