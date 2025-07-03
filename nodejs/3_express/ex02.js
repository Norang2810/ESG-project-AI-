const express = require('express');
const app = express();
// 정적 파일 경로 지정
app.use(express.static(__dirname + '/public'))
// post방식으로 데이터를 전송 시 데이터를 파싱해주는 미들웨어 : bp
app.use(express.urlencoded({extends :true}))

// 메인 페이지
app.get('/', (req, res) => {
    console.log('메인페이지')
    res.redirect('/login.html')

    /*
        sendFil(택배아저씨) vs redirect(택시아저씨) 차이점?
        -sendFile : 서버에 있는 파일을 브라우저로 직접 전송 주소값이 바뀌지 않음
                    ex)웹페이지,CSS,JS,IMG 파일 정적인 파일 제공

        -redirect : 브라우저에게 다른 주소로 가달라고 요청 주소값이 바뀐다.
                    ex)로그인 후 페이지 이동, 게시글 작성 완료 후 페이지 이동...
    */
})
// get방식으로 데이터 처리
// *express 에서 get 데이터를 꺼내는 메소드 => req.query
app.get('/getLogin', (req, res) => {
    console.log('get 요청', req.url)
    // url.parse(req.url,true).query => req.query
    console.log('변환데이터', req.query)

    // 실습
    // 입력한 닉네임이 '관리자' 라면 ,logins 페이지로
    // 그 외라면 loginF  페이지로 이동 (res.redirect 사용!)

    req.query.nick === '관리자' ? res.redirect('/loginS.html'):res.redirect('/loginF.html')
//     if (req.query.nick === "관리자") {
//         console.log('get 성공', req.url)
//         res.redirect('/loginS.html')
//     } else {
//         console.log('get 실패', req.url)
//         res.redirect('/loginF.html')
//     }
})

// post방식으로 데이터 처리
app.post("/postLogin",(req,res)=>{
    console.log('post방식 접근',req.body)
    req.body.id === 'admin' && req.body.pw === '123' ? res.redirect('/loginS.html') :  res.redirect('/loginF.html')
})

app.listen(3001, () => {
    console.log('3001 port waiting...')
})

