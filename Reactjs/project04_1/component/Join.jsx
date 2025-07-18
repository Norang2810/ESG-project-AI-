import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'
import axios from 'axios'



const Join = () => {

  const [inputId, setInputId] = useState('')
  const [inputPw, setInputPw] = useState('')
  const [inputName, setInputName] = useState('')
  const [inputMbti, setInputMbti] = useState('')
  const [inputSong, setInputSong] = useState('')

  const nav = useNavigate();

  const chPage = () => {
    // 사용자가 입력한 id,pw,nick 
    // 쿼리스트링으로 주소에 추가해보자!
    axios({
      url: 'http://localhost:3001/user/join',
      method: 'post', // 정의하지않으면 기본값 :GET방식
      data: {
        id: inputId,
        pw: inputPw,
        name: inputName,
        mbti: inputMbti,
        song: inputSong
      }
    }).then((res) => {
      //통신후 실행시킬 로직  
      console.log(res)

      // 회원가입 성공 -> 로그인 페이지
      if (res.data == 1) {
        alert('회원가입 성공!')
        nav('/login')
      } else {
        // 회원가입 실패 -> alert('회원가입 실패)
        alert('회원가입 실패!')
      }
    })

    // nav('/login?id='+inputId+'&pw='+inputPw)
    // nav(`/login?id=${inputId}&pw=${inputPw}&nick=${inputName}`)

  }



  return (

    <>
      <h1>회원가입페이지입니다.</h1>
      <div>
        ID : <input onChange={(e) => setInputId(e.target.value)} /><br />
        PW : <input onChange={(e) => setInputPw(e.target.value)} /><br />
        NAME : <input onChange={(e) => setInputName(e.target.value)} /><br />
        MBTI : <input onChange={(e) => setInputMbti(e.target.value)} /><br />
        SONG : <input onChange={(e) => setInputSong(e.target.value)}></input>
        <button onClick={chPage}>Join</button>
      </div>
    </>

  )
}

export default Join