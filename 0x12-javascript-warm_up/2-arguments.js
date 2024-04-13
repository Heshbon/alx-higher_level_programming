#!/usr/bin/node
const add = process.argv.length;
console.log(add === 2 ? 'No argument' : add === 3 ? 'Argument found' : 'Arguments found');
