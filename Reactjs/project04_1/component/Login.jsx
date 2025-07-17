import React, { useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'

const Login = () => {
    const [query,setQuery] = useSearchParams();
    const [loginId,setLoginId] = useState('')
    const [loginPw,setLoginPw] = useState('')

    const nav = useNavigate();

    const joinId = query.get('id')
    const joinPw = query.get('pw')

    const tryLogin = ()  => {
        if(loginId == joinId && loginPw == joinPw){
            alert('로그인 성공입니다.')
            nav('/random')
        }else{
            alert('로그인 실패')
            nav('/')
        }
        // 물려받은 주소 이동 기능을 사용
        // 1.사용자가 입력한 ID,PW 가져오기
        // 2.사용자가 입력한 ID와 회원가입할때 입력한 ID가 같고
        //      사용자가 입력한 PW와 회원가입할때 입력한 PW가 같다면
        //  ->'로그인 성공입니다' 알림창 출력
        // 3.사용자가 입력한 ID,PW가 둘중 하나라도 
        // 회원가입할때 입력한 ID,PW와 다르다면`
        // --> '로그인 실패' 알림창 출력
        
    }

    return (
        <>
            <div>
                <h1>즐거운 리액트 수업</h1>
                <div>
                    ID: <input type="text" onChange={(e)=>setLoginId(e.target.value)}/><br />
                    PW :<input type="text" onChange={(e)=>setLoginPw(e.target.value)}/>
                    <button onClick={tryLogin}>로그인시도</button>
                </div>
            </div>
        </>
    )
}

export default Login