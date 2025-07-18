import React from 'react'
import { AppNum } from '../App'
import { useContext } from 'react'


const LeftChild03 = () => {
    const share = useContext(AppNum)


    const chNum = () =>{
        share.setData(share.data+1);
    }

    return (
        <div>
            <h1>Left03</h1>
            <button onClick={chNum}>Plus</button>
        </div>
    )
}

export default LeftChild03