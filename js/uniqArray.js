const ary = [1, 1, "1", "1", true, true, "true", {}, {}, "{}", null, null, undefined, undefined];
//先转集合再转回数组 
let ary1 = Array.from(new Set(ary));
console.log(ary1);

//存入map的键中
const map = new Map;
ary.forEach(
  item => map.set(item, 1)
)
let ary2 = Array.from(map.keys());
console.log(ary2);

//逐个放入新数组，如果新数组中包含该元素(index不为-1||includes返回true)则跳过
let ary3= [];
ary.forEach(
  item=>ary3.includes(item)? item:ary3.push(item)
  // item=>ary3.indexOf(item)===-1? ary3.push(item):item
)
console.log(ary3);

//过滤掉indexof不等于index的元素
let ary4=
ary.filter(
  (item,index)=>ary.indexOf(item)===index
)
console.log(ary4);