// 실제로 node서버를 만들기 위해서 사용하는 모듈 =>http
// 로컬 서버를 제작할때 사용된다
// ip주소 확인 => cmd => ipconfig입력
// 코어모듈 사용
// import pandas as pd => 파이썬 라이브러리 불러오는 방식
// 모듈을 불러와서 상수에 담아주기
const http = require('http');

// 1.포트번호가 3000인 서버를 생성
// 서버를 만들때 , 두개의 매개변수가 필요 (req,res) =? request , response
// req (클라이언트가 넘겨준 데이터) , res(서버가 넘겨줄 데이터)
// listen ('포트번호') : 서버의 주소를 구별하기 위해서 

http.createServer((req,res)=>{
    console.log('누군가가 접속했어요!');


    // res데이터를 넘겨주기
    // 응답을 -> html 태그를 사용해서
    res.writeHead(200,{'Content-Type' : 'text/html; charset= utf-8'})
    res.write("<h1>오늘은 월요일</h1>")
    res.end()
}).listen(3000)



