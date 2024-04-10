#!/usr/bin/node
const add = process.argv.len;
console.log(add === 2 ? 'No argument' : add === 3 ? 'Argument found' : 'Arguments found');
