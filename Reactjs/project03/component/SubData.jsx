import React from 'react'

const SubData = ({changeData}) => {


  
    return (
        <div>
            <p>이곳은 하위(자식) 컴포넌트입니다.</p>
            <input type="text" onChange={(e)=>{changeData(e.target.value)}}/>
        </div>
    )
}

export default SubData