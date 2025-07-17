import React from 'react'
import { useSearchParams } from 'react-router-dom'; //useSearchParams : 쿼리스트링 데이터 다루는 기능

const ProDetail = () => {
    // query : 넘겨받은 쿼리스트링 데이터
    // setQuery : 넘겨받은 데이터를 수정할수있는 기능
    const [query,setQuery] = useSearchParams();
    console.log(query.get('num'))

    let queryNum = query.get('num')


  return (
    <div>
        <h1>상세보기 페이지 입니다.</h1>
        <p>{queryNum}번째 제품 상세 내용</p>
    </div>
  )
}

export default ProDetail