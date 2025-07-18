import React from 'react'
import { useContext } from 'react'
import { AppNum } from '../App'

const RightChild03 = () => {
    const share = useContext(AppNum)
  return (
    <div>
        <h1>Right03</h1>
        <p>{share.data}</p>
    </div>
  )
}

export default RightChild03