const express = require('express')
const app = express();
const mainRouter = require('./routes/mainRouter');
const subRouter = require('./routes/subRouter');


// 정적인 파일 경로 지정 (미들웨어)
app.use(express.static(__dirname + '/public'))

app.use('/',mainRouter)
/*  
`   `*Router* 
    -한파일안에서 모든 경로를 다루면 하나 파일에 의존적
    -유지보수가 어려워지고,코드의 볼륨이 비효율적
    -메인파일에는 서버생성,모듈관리,미들웨어관리 역할만!
*/
/*
    1. 어떻게 나누지?
    main
    -soccer /soccer
    -baseball   /baseball

    esports
    -lol    /esports/lol
    -fc     /esports/fc
*/

// 서브 경로
app.use('/esports',subRouter)

app.listen(3001,()=>{
    console.log("3001 wait ..")
})