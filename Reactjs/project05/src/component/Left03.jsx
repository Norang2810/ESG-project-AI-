import React from 'react'
import { useContext } from 'react'
import { AppText } from '../App'

const Left03 = () => {
    const share =useContext(AppText)
  return (
    <div>
        <h1>Left03</h1>
        <input onChange={(e)=>share.setData(e.target.value)}></input>
    </div>
  )
}

export default Left03