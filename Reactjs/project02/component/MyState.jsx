import React from 'react'
import { useState } from 'react';  //useState : state변수를 만들수있는 react기능 (Hook)


const MyState = () => {
    // 사용자의 로직에 처리되는 일반변수
    // let num =0;

    // state변수 : 화면적인 요소를 다룰 변수
    // numState : state변수
    // setNumState : state변수를 바꿀수있는 기능
    const [numState,setNumState] =useState(0);

    function plus(){
        // num++
        // console.log (num)
        setNumState(numState+1)
    }

    return (
        <div>
            <h1>{numState}</h1>
            <button onClick={plus}>PLUS</button>
        </div>
    )
}

export default MyState


