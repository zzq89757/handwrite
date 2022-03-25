// A instanceof B 的原理：若B的显示原型在A的（隐式）原型链上 则返回true
const obj = new Object();
function myInstanceOf(A, B) {
  A = A.__proto__;
  B = B.prototype;
  while (true) {
    if (A == null) return false;
    if (A == B) return true;
    A = A.__proto__;
  }
}
console.log(myInstanceOf(obj, obj));