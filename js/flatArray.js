const array = [[1, [2, [3, [4, [5]]]]]];
//直接调用flat 打平无限层
function flat(ary) {
  return ary.flat(Infinity);
}
console.log(flat(array));;
console.log("-------------------------");

function flat2(ary) {
  let string = String(ary).split(',');
  const newary = [];
  string.forEach(item => newary.push(item * 1));
  return newary;
}

console.log(flat2(array));
console.log("-------------------------");

//直接toString
function flat3(ary) {
  let str = "["+ary.toString().split(',')+"]";
  const newary = JSON.parse(str);
  return newary;

}
console.log(flat3(array));

//先转成json字符串加上中括号再转回json数组
function flat4(ary){
  let newary = JSON.parse("["+JSON.stringify(ary).replace(/\[|\]/g,'')+"]");
  return newary;
}
console.log(flat4(array));