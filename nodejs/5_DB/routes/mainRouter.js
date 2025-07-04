const exprees = require('express')
const router = exprees.Router()

const path = require('path')
const file_path = path.join(__dirname,'..','public')



router.get('/',(req,res)=>{
    console.log('메인페이지 접속!')
    res.sendFile(file_path+'/main.html')
})


router.get('/join',(req,res)=>{
    console.log('회원가입 페이지로 이동성공!')
    res.sendFile(file_path+'/join.html')
})
router.get('/login',(req,res)=>{

    // sendFile /login
    // redirect /login/login.html
    console.log('회원가입 페이지로 이동성공!')
    res.sendFile(file_path+'/login.html')
})
router.get('/delete',(req,res)=>{
    console.log('회원삭제 페이지로 이동성공!')
    res.sendFile(file_path+'/delete.html')
})
router.get('/update',(req,res)=>{
    console.log('회원수정 페이지로 이동성공!')
    res.sendFile(file_path+'/update.html')
})




module.exports = router



