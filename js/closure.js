var a = 100;
function outter(){
  var a=6;
  function inner(){
    a++;
    console.log(a);
  }
  inner()
}
console.log(a);
outter()
outter()
outter()