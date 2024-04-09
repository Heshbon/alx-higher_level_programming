#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (num, now) {
    num.push(now);
    return num;
  }, []);
};
