
import React from 'react'

export const Map = () => {

    // map함수
    // -주어진 함수를 호출한 결과를 통해서 새로운 배열을 반환한다.
    // let 새로운 배열이름 = 배열이름.map((매개변수)=> (리턴식))
    // *반드시 key값이 포함, 그 key값은 고유해야한다.
    // 그래서 key값은 보통 DB의 PK값 ,고유번호 사용

    let num = [1, 2, 3, 4, 5]
    let newNum = num //num이라는 배열을 호출해서
        .map( //새로운 배열을 만들어줄게
            (item) => //안에 있는 애들 싹 가져와서
                (item * 10) //10 곱해서 내보낼거야 =>newNum으로
        )
    console.log('newNum : ', newNum)


    let tc = ['선영표', '장영우', '신정욱', '임승환']
    let newtc = tc.map(item => <button key={item}>{item}선생님</button>)
    console.log('newTc :', newtc)


    // 보통은 배열 + 객체 혼합
    let list = [
        { name: '선영표', bloodType: 'A', age: 20 },
        { name: '장영우', bloodType: 'B', age: 20 },
        { name: '신정욱', bloodType: 'O', age: 20 },
    ]

    // let nameList = list.map(item=>item.name)
    // let bloodList = list.map(item=>item.bloodType)
    // let ageList = list.map(item=>item.age)

    // <p>안녕하세요 저는 선영표입니다 . 저는 A형이고 20살입니다.</p>

    // for(let i =0; i<list.length;i++){
    //     console.log('안녕하세요 저는 ' + nameList[i] +'입니다. 저는' + bloodList[i] + '형이고 ' + ageList[i] + '입니다' )
    // }

    let newList = list.map(item => <p key={item.name}>안녕하세요. 저는 {item.name}입니다. 저는 {item.bloodType}형이고 {item.age} 입니다.</p>)

    // title,birthYear,content,imgSrc,SNS

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
    let newDataList = dataList.map(item =>
        <div key={item.title}>
            <h2>{item.title}</h2>
            <p>{item.content}</p>
            <img src={item.imgSrc} /><br />
            <a href={item.SNS}>SNS 보기</a>
        </div>
    );

    return (
        <div>
            <div>
                <p>{newtc}</p>
            </div>
            <div>
                <p>{newList}</p>
            </div>
            <div>            
                <img width='300px' />
                {newDataList}
            </div>
        </div>
    )
}



export default Map