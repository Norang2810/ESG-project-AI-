// Node 를 실행하는 방법
// 1. Ctrl + ` -> 터미널 오픈 단축키
// 2. 상단 좌측 탭 - >Termianl -> New Terminal
// 3. *가장중요!! -> 반드시 실행할 파일의 경로를 확인하기!!



let { odd, even } = require('./var');

console.log(odd);


let num =4;

let result = num%2 ===0? even : odd
console.log(result)