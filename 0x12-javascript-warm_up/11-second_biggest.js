#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const value = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((j, k) => j - k);
  console.log(value[value.length - 2]);
}
