// 컴포너트 : 리액트 프로젝트에서 사용자에게 화면을 보여줄수있는 수단
//                 (사용자 정의 태그)

import React from 'react'

// 1.컴포넌트 함수 생성
function Menu(props) {
    // props :  상위 컴포넌트가 현재 컴포넌트로 넘긴 데이터

    console.log(props)
    return (
        <div>  
            <h1>{props.mName}</h1>
            <p>{props.price}</p>
        </div>
        
    )
}
// 2.컴포넌트 내보내기
export default Menu