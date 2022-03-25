function Foo(){
  var i =0;
  j=0;
  return function(){
    console.log(i++);
    console.log(j++);
  }
}

var f1 = Foo();
f2 = Foo();
f1();
f1();
f2();
f2();