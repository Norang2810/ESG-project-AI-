import React from 'react'

const Myteam = (props) => {


    let myStyle ={
        border : '10px solid',
        backgroundColor : 'green'

    }
    return(
        <div style={myStyle}>
            <div>{props.dept}</div>
            <div>{props.dName}</div>
        </div>
    )
}

export default Myteam