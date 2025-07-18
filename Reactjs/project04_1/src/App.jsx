import { useState } from 'react'
import './App.css'
import { Route, Routes } from 'react-router-dom'
import Join from '../component/Join'
import Login from '../component/Login'
import MyRandom from '../component/MyRandom'
import ProHome from '../component/ProHome'
import ProDetail from '../component/ProDetail'
import LoginS from '../component/LoginS'
import LoginF from '../component/LoginF'

function App() {


  return (
    <>
          <Routes>
            <Route path='/' element = {<Join></Join>}></Route>
            <Route path='/login' element = {<Login></Login>}></Route>
            <Route path='/random' element = {<MyRandom></MyRandom>}></Route>
            <Route path='/prohome' element = {<ProHome></ProHome>}></Route>
            <Route path='/prodetail' element = {<ProDetail></ProDetail>}></Route>
            <Route path='/logins' element = {<LoginS></LoginS>}></Route>
            <Route path='/loginf' element = {<LoginF></LoginF>}></Route>
          </Routes>
          
    </>
  )
}

export default App
