import { useState } from 'react'
import './App.css'
import Left01 from './component/Left01'
import Right01 from './component/Right01'
import { createContext } from 'react'

// Context : 데이터 공유공간 
// 1.createContext() : 공유 공간 생성
// 2. export : 공유공간 내보내기

export const AppText = createContext()

function App() {

  const [myData, setMyData] = useState('공유데이터')

  return (
    // 3. AppText라는 공유공간을 사용할수 있게끔 허용.
    <>
      <AppText.Provider value={{
        data: myData,
        setData : setMyData
      }}> 
      {/* 4. value 속성으로 공유공간에 공유할 데이터 지정 */}
        <Left01></Left01>
        <Right01></Right01>
      </AppText.Provider>
    </>
  )
}

export default App
