const express = require('express')
const router = express.Router()
// DB연결
const conn = require('../config/db')

// 회원가입의 *기능* 라우팅
// http://localhost:3001/user/join
router.post('/join', (req,res)=>{
    console.log('접근 확인')
    console.log('user join',req.body)
    let {id,pw,name,mbti,song} =req.body    //비구조화 할당 개념.
    console.log('ID :',id)

    // 사용자의 정보를 DB에 넣어야한다! ->MySQL 사용
    
    let sql = "INSERT INTO NODEJS_MEMBER VALUES (?,?,?,?,?)"
    conn.query(sql,[id,pw,name,mbti,song], (err,rows)=>{
        console.log('rows',rows)
        if(rows.affectedRows>0){
            // res.redirect('/')
            res.json(1) //<-응답을 json형태로 함.
        }else{
            res.json(0)
            // res.send('<script>alert("회원가입 실패!");window.location.href="http://localhost:3001/login"</script>')
        }

    })
})


module.exports = router