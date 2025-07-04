const express = require('express')
const app = express();
const mainRouter = require('./routes/mainRouter');
const userRouter = require('./routes/userRouter');

app.use(express.static(__dirname+'/public')) //정적파일 미들웨어 

// post방식 시 데이터 변환을 위한 미들웨어
app.use(express.urlencoded({extends : true}))

app.use('/',mainRouter)
app.use('/user',userRouter)


app.listen(3001,()=>{
    console.log("3001 wait ..")
})