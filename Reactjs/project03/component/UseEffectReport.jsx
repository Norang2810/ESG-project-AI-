import { useEffect, useState } from 'react'


const UseEffectReport = () => {

    // 1.random 수 생성 1~50
    // 2.추측이라는 버튼 클릭시 input태그에 적은 숫자와 random숫자 비교
    // 3.비교시 입력한 숫자가 더 크다면 기회 -1 , hint: 더 작은 숫자 입력
    // 4.비교시 입력한 숫자가 더 작다면 기회 -1 , hint: 더 큰 숫자 입력
    //  * 총 기회 수 : 5 
    // 5. 5번안에 맞췄을때만 결과로 '정답' 출력
    // 6. 5번 넘었다면 결과로 '땡' 으로 출력
    let comRanNum = parseInt(Math.random() * 50) + 1
    console.log(comRanNum)
    const [inputNum, setInputNum] = useState('')
    // setState함수가 실행되면 재렌더링 된다.
    // --> 컴포넌트 함수가 재실행된다.
    // -->주의! state값은 재렌더링에 영향을 안받는다.
    const [ranNum, setRanNum] = useState(comRanNum)
    const [chance, setChance] = useState(5)
    const [hint, setHint] = useState('')
    const [result, setResult] = useState('')

    // useEffect : 화면 내용이 바뀌면 (state값이 바뀌면 실행 하겠다.)

    useEffect(() => {
        if (chance >= 0) {
            if (inputNum === ranNum) {
                setResult('정답입니다.')
            }
        }
        else {
            setResult('횟수 초과입니다.')//횟수 초과
        }
    }, [chance])

    const gameStart = () => {
        if (inputNum > ranNum) {
            setHint('더작은 숫자 입력!')
        } else if (inputNum < ranNum) {
            setHint('더 큰 숫자 입력!')
        }
        setChance(chance - 1)

    }


    return (
        <div>
            <h1>1~50랜덤 수 맞추기</h1>
            <div>
                <p>
                    기회 : {chance}
                </p>
            </div>
            <input onChange={(e) => setInputNum(e.target.value)}></input>
            <button onClick={gameStart}>추측</button>
            <p> hint:{hint} </p>
            <h1>결과 : {result}</h1>
        </div>


    )
}

export default UseEffectReport