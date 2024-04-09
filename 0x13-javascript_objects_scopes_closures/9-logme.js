#!/usr/bin/node
let b = 0;
exports.logMe = function (value) { console.log(`${b++}: ${value}`); };
