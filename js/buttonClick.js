var btns = document.getElementsByTagName('button');
// for (var i = 0; i < btns.length; i++) {
//   btns[i].addEventListener('click', function () {
//     console.log(`第${i}个按钮被点击了`)
//   })
// }
for (var i = 0; i < btns.length; i++) {
  (function (i) {
    btns[i].addEventListener('click', () =>
      console.log(`第${i}个按钮被点击了`))
  })(i)
}
