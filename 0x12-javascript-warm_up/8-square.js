#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < size; a++) {
    let line = '';
    for (let b = 0; b < size; b++) line += 'X';
    console.log(line);
  }
}
