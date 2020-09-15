#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = myfunc;
function myfunc () {
  myObject.value++;
}

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
