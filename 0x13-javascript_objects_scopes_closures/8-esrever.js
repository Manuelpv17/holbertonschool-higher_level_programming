#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let i = 0; i < list.length; i++) {
    newList.push(list[list.length - i - 1]);
  }
  return newList;
};
