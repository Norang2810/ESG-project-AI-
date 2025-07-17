import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'

const Join = () => {

  const [inputId, setInputId] = useState('')
  const [inputPw, setInputPw] = useState('')
  const [inputNick, setInputNick] = useState('')


  const nav = useNavigate();

  const chPage = () => {
    // 사용자가 입력한 id,pw,nick 
    // 쿼리스트링으로 주소에 추가해보자!
    // nav('/login?id='+inputId+'&pw='+inputPw)
    nav(`/login?id=${inputId}&pw=${inputPw}&nick=${inputNick}`)
  }



  return (

    <>
      <h1>회원가입페이지입니다.</h1>
      <div>
        ID : <input onChange={(e) => setInputId(e.target.value)} /><br/>
        PW : <input onChange={(e) => setInputPw(e.target.value)} /><br/>
        NICK : <input onChange={(e) => setInputNick(e.target.value)} /><hr/>
        <button onClick={chPage}>Join</button>
      </div>
    </>

  )
}

export default Join