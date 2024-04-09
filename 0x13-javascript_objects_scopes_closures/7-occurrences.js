#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((add_up, now) => now  === searchElement ? add_up + 1 : add_up, 0);
};
