import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Data from '../component/Data'
import RSP from '../component/RSP'
import UseEffect from '../component/UseEffect'
import UseEffectReport from '../component/UseEffectReport'
import MyAxios from '../component/MyAxios'

function App() {
  
  return (
    <>
    {/* 데이터 양방향 통신 */}
      {/* <Data></Data> */}
      {/* LifeCycle */}
      {/* <RSP></RSP> */}
      {/* <UseEffect></UseEffect> */}
      {/* <UseEffectReport></UseEffectReport> */}
      <MyAxios></MyAxios>
    </>
  )
}

export default App
