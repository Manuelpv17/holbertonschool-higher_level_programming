#!/usr/bin/node

exports.converter = function (base) {
  function toBase (number) {
    return number.toString(base);
  }
  return toBase;
};
