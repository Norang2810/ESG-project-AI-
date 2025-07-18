import React, { useEffect } from 'react'
import axios from 'axios'
import { useState } from 'react'




const MyAxios = () => {

    // 1.처음 페이지에 들어가게 되면 2020년 01월 01일 기준으로 영화 데이터 출력
    // --> useEffect //맨처음 화면이 띄어졌을때 , state이 바뀌었을때 , [] <= 의존성배열

    useEffect(() => {
        axios({
            url: 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=a758f2ab23ce7d23519758bd10b1def7&targetDt=20200101',
            method: 'GET'
        })
            .then((res) => {
                setMovieData(res.data.boxOfficeResult.dailyBoxOfficeList)
            })
    }, [])

    const [movieData, setMovieData] = useState([])
    const [inputData, setInputDate] = useState('')

    const getData = () => {
        axios({
            url: `http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=a758f2ab23ce7d23519758bd10b1def7&targetDt=${inputData}`,
            method: 'GET'
        })
            .then((res) => {
                console.log('통신성공')
                console.log(res.data.boxOfficeResult.dailyBoxOfficeList)  // 확인용
                setMovieData(res.data.boxOfficeResult.dailyBoxOfficeList)
            })
            
            

    }

    return (
        <div>
            <h1>영화 데이터 비동기 통신(Axios)</h1>
            <input onChange={(e)=>setInputDate(e.target.value)} />
            <button onClick={getData}>데이터 가져오기</button>
            <table border="1" >
                <thead>
                    <tr>
                        <td>영화순위</td>
                        <td>제목</td>
                        <td>개봉일</td>
                    </tr>
                </thead>

                {/* map()함수 : 배열안에 요소를 한번씩 순차적으로 전부 접근해서 모든 항목의 데이터를 원하는형식으로 바꿔주는 함수 */}
                {/* item : map함수를 통해서 접근한 배열의 요소 */}
                <tbody>
                    {movieData.map((item) =>
                        <tr key={item.movieCd}>
                            <td>{item.rank}</td>
                            <td>{item.movieNm}</td>
                            <td>{item.openDt}</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    )
}

export default MyAxios