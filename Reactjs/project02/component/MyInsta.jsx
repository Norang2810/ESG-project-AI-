import React, { useState } from 'react';
import img1 from '../src/img/img1.jpeg';    
/*
        React에서 이미지를 띄우는 방법 3가지
        1.외부 주소 사용 
        2.src폴더 사용 
            -import 별칭 from '경로'
            -장점 : 경로처리에 유리하다
            -단점 : 여러개의 이미지를 한번에 가져올때 불편함.
            -로고나 컴포넌트에 늘 떠있는 이미지를 사용할때 추천
        3.public폴더 사용
            -public 폴더는 폴더 그자체로 이미 서버와 통신중
            -public 폴더에 자료를 보관하는 것 만으로도 이미 본인의 주소가 생김
            => "http://localhost:5173/img/img2.jpeg"
            => "/img/img2.jpedg" (생략 가능)

            -장점 : 동적 접근이 쉽다. 파일 변경에 용이함.
            -단점 : 불필요하게 public 폴더의 파일들이 노출
                =>민감한 파일, 사내 중요 이미지 등 보안이 필요한 이미지 X ,
                    경로 오류가 있더라도 배포단계에서 잡아내지 못함.
*/


// 1.하트를 클릭했을때 실행될 함수 handleLike를 생성
// 2. handleLike 실행 시,
// 조건 : 값이 바뀔때마다 화면이 바로바로 바뀌어야함.
//  - 사용되는 state의 이름 -> emoji(하트기호) , likeNum(숫자)
//  - if문 사용


// const MyInsta = () => {
//     let [likeNum, setLikeNum] = useState(0);
//     let [emoji, setEmoji] = useState("🤍"); // 기본값: 흰 하트

//     function handleLike() {
//         if (likeNum === 0) {
//             setLikeNum(1);
//             setEmoji("❤️");
//         } else {
//             setLikeNum(0);
//             setEmoji("🤍");
//         }
//     }

//     return (
//         <div>
//             <img width='300px' src={img1} alt="인스타사진" />
//             <p>
//                 <span onClick={handleLike}>{emoji}</span>
//                 {" "} 
//                 좋아요 
//                 {" "}
//                 <span onClick={handleLike}>{likeNum}</span> 
//                 개
//             </p>
//         </div>
//     );
// };

// export default MyInsta;



// const MyInsta = () => {

//     const [likeNum, setLikeNum] = useState(0);
//     const [emoji, setEmoji] = useState("🤍");

//     function handleLike() {
//         if (likeNum === 0) {
//             setLikeNum(1);
//             setEmoji('❤️')
//         } else {
//             setLikeNum(0);
//             setEmoji('🤍')
//         }
//     }


//     return (
//         <div>
//             <img width='300px' src={img1} alt="인스타사진" />
//             <p>
//                 <span onClick={handleLike}>{emoji}</span>
//                 {" "}
//                 좋아요
//                 {" "}
//                 <span onClick={handleLike}>{likeNum}</span>
//                 개
//             </p>
//         </div>
//     )
// }

// export default MyInsta


const MyInsta = () => {

    const [emoji, setEmoji] = useState('🤍')
    const [likeNum, setlikeNum] = useState(0)

    function handleLike() {
        if (likeNum === 0) {
            setlikeNum(1)
            setEmoji('❤️')
        } else {
            setlikeNum(0)
            setEmoji('🤍')
        }
    }



    return (
        <div>
            <img img width='300px' src={img1} />
            <p>
                <span onClick={handleLike}>{emoji}</span>
                {" "}
                좋아요
                {" "}
                <span onClick={handleLike}>{likeNum}개</span>
            </p>
        </div>
    )
}

export default MyInsta