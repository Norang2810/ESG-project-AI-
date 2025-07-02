const http = require('http');
const m_url = require('url');
const qs = require('querystring'); // 문자열을 queryString형태로 변환(name,value값으로 분석)
const { Script } = require('vm');

http.createServer((req, res) => {
    console.log('누군가가 서버에 접근!')

    // 사용자가 입력한 값을 어딘가에 누적 : on

    var body = ""
    req.on('data', (data) => {
        body += data
        console.log('body :', body)
    })

    // 사용자가 입력한 데이터 수신이 끝났을때 데이터를 출력 : end

    req.on('end', () => {
        var post = qs.parse(body)
        console.log('post :', post.id)
        console.log('post :', post.pw)
        
        // 사용자에게 응답
        // 환영합니다 000(ID)님, 당신의 비밀번호는 0000(PW)입니다
        res.writeHead(200,{"Content-Type" : "text/html;charset=utf-8"})
        res.write('<html><body>')
        res.write(`환영합니다 ${post.id}님, 당신의 비밀번호는 ${post.pw}입니다.`)
        res.write('</body></html>')
    })


    

})
    .listen(3001)