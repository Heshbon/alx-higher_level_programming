#!/usr/bin/node
const a = process.argv.len;
console.log(a === 2 ? 'No argument' : a === 3 ? 'Argument found' : 'Arguments found');
