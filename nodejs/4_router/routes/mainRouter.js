// 경로 : 실제 스포츠 경로 페이지

const express = require('express');
const router = express.Router();

const path = require('path'); //경로 수정시 사용
const file_path = path.join(__dirname,'..','public') 
// 메인페이지
router.get('/',(req,res)=>{
    // res.sendFile('') 
    console.log('메인에 접속했습니다.')
    res.sendFile(file_path+'/main.html')

    // ERROR Case
    // 현재 작업중인파일이 routes폴더 안에 있기 때문에
    // 전에 했던것과 달리 한번 상위폴더로 올라가줘야함
    // =>path모듈을 이용해서  -> 절대경로 만들어야함.
})
// 축구페이지로 이동
router.get('/soccer',(req,res)=>{
    res.sendFile(file_path+'/soccer.html')
    console.log('축구페이지 이동 성공!')
})
// 야구페이지로 이동
router.get('/baseball',(req,res)=>{
    res.sendFile(file_path+'/baseball.html')
    console.log('야구페이지 이동 성공!')
})


// 이 라우터 모듈을 외부에서 사용해야하기때문에 exports작업 필요
module.exports= router;