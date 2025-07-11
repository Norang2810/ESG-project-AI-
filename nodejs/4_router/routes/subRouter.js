const express = require('express')
const router = express.Router()
const path=require('path')
const file_path = path.join(__dirname,'..','public')

// esports 서브라우터
// 여기에 적는 경로들은 앞에 /esports 가 붙음
router.get('/',(req,res)=>{
    console.log('E스포츠 페이지입니다.')
    res.sendFile(file_path+'/esports.html')
})
// FC 라우터
router.get('/fc',(req,res)=>{
    console.log('FC 페이지입니다.')
    res.sendFile(file_path+'/fc.html')
})
// LOL라우터
router.get('/lol',(req,res)=>{
    console.log('LOL페이지 이동성공!')
    res.sendFile(file_path+'/lol.html')
})


module.exports = router;