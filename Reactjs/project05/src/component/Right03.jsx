import React from 'react'
import { useContext } from 'react'
// useContext : createContext로 만들어진 공유 공간에 접근 할수있는 기능(훅)
import { AppText } from '../App' //주의! 어떤 공유공간을 사용할지 명시해야함.

const Right03 = () => {
    //공유 공간에 접근해서 값을 가지고옴.
    const shareData = useContext(AppText)
    console.log(shareData)
    
    return (
        <div>
            <h1>Right03</h1>
            <h1>{shareData.data}</h1>
        </div>
    )
}

export default Right03