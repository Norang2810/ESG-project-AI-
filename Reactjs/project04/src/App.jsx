import { useState } from 'react'
import './App.css'
import Home from '../component/Home'
import About from '../component/About'

import { Route, Routes } from 'react-router-dom'

// router : 주소값을 기준으로 다른페이지 (다른컴포넌트를 실행 시키겠다.)
function App() {

  return (
    //   =>  / 주소값으로 접근했을때 Home컴포넌트를 출력
    <>
      <Routes>
        <Route path='/' element={<Home></Home>}></Route>
        {/*  /about으로 접근했을때 About컴포넌트를 출력 */}
        <Route path='/about' element={<About></About>}></Route>
      </Routes>
    </>
  )
}

export default App
