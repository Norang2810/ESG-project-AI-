import React from 'react'
import { useSearchParams } from 'react-router-dom'


const LoginS = () => {

    const [query,setQuery] = useSearchParams();   

    return (
        <div>
            <h1>로그인성공</h1>
            <h2>{query.get('nick')}님 환영합니다!</h2>
        </div>
    )
}

export default LoginS