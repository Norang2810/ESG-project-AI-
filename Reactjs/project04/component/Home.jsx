import React from 'react'
import { Link } from 'react-router-dom'
import { useNavigate} from 'react-router-dom'
const Home = () => {
    return (
        <div>
            <h1>Home페이지입니다.</h1>
            <a href="/about">about페이지이동</a><br />
            {/* 리액트에서는 Link to = 'url주소'  => 새로고침이 되지않음. Link사용 추천*/}
            <Link to='/about'>About이동 2</Link> 
        </div>
    )
}

export default Home