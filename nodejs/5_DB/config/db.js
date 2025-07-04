// DB에 대한 정보


const mysql = require('mysql2')
const conn = mysql.createConnection({
    host : 'localhost' 
    ,port : 3306 
    ,database : 'nodejs'
    ,password : '1234' 
    ,user : 'root'
})

conn.connect()
console.log('DB연결 성공!')
module.exports =conn;
