function curry(...arguments){
  let arg = arguments.shift();
  console.log(arg);
  if(arguments.length==0){
    return
  }
  return function(...arguments){
    curry(...arguments)
  }
}
console.log(curry(1)(2));