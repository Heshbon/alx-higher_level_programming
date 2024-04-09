#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((add, now) => now === searchElement ? add + 1 : add, 0);
};
