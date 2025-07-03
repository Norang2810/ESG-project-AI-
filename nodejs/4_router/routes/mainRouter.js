// 경로 : 실제 스포츠 경로 페이지

const express = require('express');
const router = express.Router();

router.get('/',(req,res)=>{
    // res.sendFile('') 
    console.log('메인에 접속했습니다.')
})

// 이 라우터 모듈을 외부에서 사용해야하기때문에 exports작업 필요
module.exports= router;