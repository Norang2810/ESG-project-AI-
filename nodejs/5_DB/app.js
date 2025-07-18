const express = require('express')
const app = express();
const mainRouter = require('./routes/mainRouter');
const userRouter = require('./routes/userRouter');
const cors = require('cors')

app.use(cors())
app.use(express.static(__dirname+'/public')) //정적파일 미들웨어 

// post방식 시 데이터 변환을 위한 미들웨어
app.use(express.urlencoded({extends : true}))
app.use(express.json())  // <-axios로 통신하고 data 키값을 가져올때 axios는 애초에 객체로 가져온다는건데
// 그러기위해선 이 한줄을 명시해줘야한다.
app.use('/',mainRouter)
app.use('/user',userRouter)


app.listen(3001,()=>{
    console.log("3001 wait ..")
})