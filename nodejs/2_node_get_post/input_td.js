const { write } = require('fs');
const http = require('http')
const url = require('url')
//서버만들기
http.createServer((req,res)=>{
    const queryData = url.parse(req.url,true).query
    console.log(queryData);

    res.writeHead(200,{'content-type' :'text/html;charset=utf8'})
    //table 태그는 => 표 형태를 만들 때 사용
    // 한 줄을 만들 때 => tr
    // 한칸을 만들 때 -> td
    res.write('<table border=1>')
    res.write('<tr bgcolor=yellow>')
    for(let i=0;i<queryData.inputTd; i++){
        res.write(`<td>${i+1}</td>`)
    }
    res.write('</tr>')
    res.write('</table>')
}).listen(3001)