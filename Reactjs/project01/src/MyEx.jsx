import React from 'react'

const MyEx = () => {

    /* 1.사용자로 부터 월~일 요일을 입력받는다
       2.월요일을 제외한 다른 요일이 입력 됐다면 (검은색글씨)출력
       3.월요일이 입력되면 빨간색 글씨로 출력 시켜줴요.
    */
    
    let day = prompt('요일을 입력하세요')
    console.log(day)
    

    let myColor ='black'
    if(day === "월요일"){
        myColor ='red'
    }

    let myStyle = {
        color : myColor
    }

  return (
    <div>
         <h1 style={myStyle}>진우님 , 오늘은 {day} 입니다.</h1>
    </div>
  )
}

export default MyEx