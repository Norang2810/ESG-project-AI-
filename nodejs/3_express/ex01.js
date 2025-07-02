/*
| 용어             | 설명                                                           
| -------------- | ---------------------------------------------------------------- |
| **JavaScript** | 원래는 브라우저에서 돌아가는 프로그래밍 언어 |                                        
| **Node.js**    | JavaScript를 브라우저 밖, 즉 서버에서 실행 가능하게 만든 런타임 환경|
| **Express.js** | Node.js 위에서 동작하는 웹 서버 프레임워크<br> (라우팅, 미들웨어, 요청/응답 처리 등 간편화)|
 */


/*
    [Express설치 방법]
    1.node서버 설치 선행
    2.express를 사용할 서버 파일이 있는 폴더 이동
    3.(터미널) npm init -y
        -package.json 이라는 파일을 생성해주는 명령어
    4.npm install express
    =>설치완료
*/


// 목표 : express 이용해서 서버 생성
const express = require('express')
const app = express()
// 정적인 파일의 경로를 지정(미들웨어)
app.use(express.static(__dirname+'/static'))

// get으로 요청시 작성한 텍스트를 응답
// app.get(경로,콜백함수)


// 누군가가 서버주소에 "/"를 요청한다면~
app.get('/',(req,res)=>{
    res.send('express page')
})
// 누군가가 서버주소에 "/mypage"를 요청한다면~
app.get('/mypage',(req,res)=>{
    res.sendFile(__dirname+'/ex01mypage.html')

    // dir (directory) name (name) : 현재 파일이 위치한 폴더의 절대경로
    // 정적인 파일들을 포함하는 폴더를 특정할때 많이 사용


})



// app.listen은 항상 서버파일의 가장 하단에 있어야함.
// 3001번 포트로 오는 요청을 기다리는중...
app.listen(3001,()=>{
    console.log('3001 port waiting...')
})

