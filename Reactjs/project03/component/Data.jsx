import { useState } from 'react'
import SubData from './SubData'

const Data = () => {

    /*  목표 : 하위 컴포넌트에서 상위 컴포넌트로 값을 전달해보자.
            -React는 기본적으로 단방향 데이터 흐름을 가지고 있기 때문에
                상위=> 하위로의 데이터 전달은 props를 통해 가능
                하위 =>상위로의 데이터 전달은 불가능하다.

        [하위 => 상위]
        1.상위 컴포넌트에서 함수를 생성
        2.하위컴포넌트한테 props로 함수 전달
        3.하위 컴포넌트는 전달 받은 함수의 매개변수에 값을넣는다.
        4.상위 컴포넌트로 넘어온 매개변수 값을 전역변수에 넣어서 사용.

        ** 전역적으로 데이터를 관리할수있는 Context API 나 Redux 를 활용하면 더욱 편함. -> 책 393p , 411p 까지.
    */

    const [text,setText] = useState('여기에 입력된 값이 보여요')


    const changeData = (value) => {
        console.log('changeData 함수 호출', value)
        setText(value)
    }


    return (
        <div>
            {text}
            <hr></hr>
            <SubData changeData={changeData}></SubData>
        </div>

    )
}

export default Data