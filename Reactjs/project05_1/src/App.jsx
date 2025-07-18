import { useState } from 'react'
import './App.css'
import LeftChild01 from './component/LeftChild01'
import RightChild01 from './component/RightChild01'
import { useContext } from 'react'
import { createContext } from 'react'


export const AppNum = createContext();

function App() {

  const [btnPlus, setbtnPlus] = useState(0)



  return (
    <>
      <AppNum.Provider value={
        {
          data: btnPlus,
          setData: setbtnPlus
        }
      }>
        <LeftChild01></LeftChild01>
        <RightChild01></RightChild01>
      </AppNum.Provider>
    </>
  )
}

export default App
