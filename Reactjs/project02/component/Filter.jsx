
import React from 'react'

const Filter = () => {

    //Filter함수란 ? (JS 내장 배열함수)
    //-> 주어진 함수의 테스트를 통과하는 요소들만 모아서 새로운 배열로 반환
    // 그룹의 유닛
    // 그룹에 유닛이 새로 만들어졌다고 해서 그룹이 해체하는건 아님
    //  => filter 함수로 새로운 배열이 만들어졌다고 해서 기존배열에 이상이 가는 것은 X

    let num = [1, 2, 3, 4, 5]

    let oddNum = num.filter(item => item % 2 === 1)
    console.log('num : ', num)
    console.log('oddNum : ', oddNum)

    let words = ['오렌지', '자몽', '히비스커스']
    let longWords = words.filter(item => item.length > 2)
    console.log('words : ', words)
    console.log('longWords : ', longWords)


    let list = [
        { name: '선영표', bloodType: 'A', age: 20 },
        { name: '장영우', bloodType: 'B', age: 20 },
        { name: '신정욱', bloodType: 'O', age: 20 },
    ]

    //1. list에서 혈액형이 A형인 사람만 뽑아서 (filter)
    let aList = list.filter(item => item.bloodType === 'A')
    console.log('aList', aList)
    //2. 화면에 p태그로 소개글을 출력(map)
    let newAList = aList.map(item =>
        <p key={item.name}>안녕하세요 저는  {item.name}이고 ,{item.bloodType}형입니다.</p>
    )

    // 실습 **
    // birthYear 가 1994보다 작거나 같은 사람만 출력

    // find함수
    // 배열의 요소를 순차적으로 순회하면서 조건에 일치하는 요소의 값을 즉시 반환
    //filter => 배열로 반환   , find => 객체로 반환
    let fList = list.find(item => item.bloodType === 'A')
    console.log('fList',fList)

    let dataList = [
        {
            "title": "아이유 (IU)",
            "birthYear": 1993,
            "content": "대한민국의 가수 겸 배우. 15세였던 중학교 3학년 때 2008년에 가수로 데뷔했으며, 예명인 '아이유'는 '음악으로 너와 내가 하나가 된다'라는 뜻을 가지고 있다.",
            "imgSrc": "https://mblogthumb-phinf.pstatic.net/MjAxNzA5MDdfMjQ1/MDAxNTA0NzY2MTg3NjMw.082G5PddLUVM6x35yJ5Ex6lKonxHrf_tf7lJHjEijYsg.WSzLj8tTAdxrZqXxMMutfLdOE-P7oNKK80_asLRlEmAg.PNG.morning1377/%EC%95%84%EC%9D%B4%EC%9C%A0_%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8_%EA%B7%BC%ED%99%A9.PNG?type=w2",
            "SNS": "https://www.instagram.com/dlwlrma"
        },
        {
            "title": "수지 (Suzy)",
            "birthYear": 1994,
            "content": "대한민국의 가수이자 배우. 2010년 데뷔한 JYP 소속의 걸그룹 미쓰에이의 원년 멤버다. 2011년 드림하이로 처음 연기 데뷔를 했고 2019년부터 매니지먼트 숲 소속으로 연기자와 유튜버로 활동하고 있다.",
            "imgSrc": "https://newsimg.sedaily.com/2019/09/04/1VO45O5N53_3.jpg",
            "SNS": "https://www.instagram.com/skuukzky"
        },
        {
            "title": "나연 (Nayeon)",
            "birthYear": 1995,
            "content": "대한민국의 가수. JYP엔터테인먼트 소속 9인조 그룹 TWICE의 맏언니이며, 리드보컬과 리드댄서를 맡고 있다.2022년 6월 24일 첫 미니 앨범인 IM NAYEON을 발매하며 솔로 활동을 시작했다.",
            "imgSrc": "https://cphoto.asiae.co.kr/listimglink/1/2022021015065139442_1644473211.jpg",
            "SNS": "https://www.instagram.com/nayeonyny"
        }
    ]

    let bYear = dataList.filter(item => item.birthYear <= 1994)
    console.log('bYear', bYear)

    let lastList = bYear.map(item => (
        <div key={item.title}>
            <img width='100px' src={item.imgSrc}></img>
            <h2>{item.title}</h2>
            <p>{item.content}</p>
            <a href={item.SNS}>인스타그램으로 이동</a>
        </div>
    ))
    return (
        <div>
            <>
                {newAList}
                {lastList}
            </>
        </div>
    )
}


export default Filter