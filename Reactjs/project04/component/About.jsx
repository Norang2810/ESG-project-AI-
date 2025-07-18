import React from 'react'
// useNavigate : 주소값을 바꿀수 있는 기능 (React Hook)
import { useNavigate } from 'react-router-dom'



const About = () => {

    const nav = useNavigate();
    const chPage = ()=>{
        nav('/')
    }


    return (
        <div>
            <h1>About페이지입니다.</h1>
            <button onClick={chPage}>홈페이지로 이동</button>
        </div>
    )
}

export default About