import './App.css'



function App() {
  /* 4. StrictMode : 검토용모드
       -React Project를 2번 실행
     -main.jsx로 이동해서 삭제
    
     5.class 대신 className을 사용함

     6.끝태그 생략 불가
     =><br></br>   (0)
     =></br>       (0)
     =><br>        (X)

     7.스타일링  적용 방법 2가지
     -기존처럼 css로 적용
     -스타일 객체를 속성에 적용


    */
  let name = prompt('이름을 입력하세요.')

  let score = 90
  let grade = 'B'

  if(score >90){
    grade = 'A'
  }else if (score > 80){
    grade = 'B'
  }else if (score >70){
    grade = 'C'
  }else {
    grade = 'F'
  }
// 사용자의 요청에 따라 동적으로 변하는값이면 객체로 스타일 지정하면 편함.
  let divStyle ={
    backgroundColor : 'lightpink',
    fontSize : '30px'
  }
  return (
    <>
    {/* [3-1] */}
         <div style={divStyle}>{name}님의 
          {name === "선영표" ? "React" : "딥러닝"}
           페이지입니다. </div>
      <div>환영합니다. </div>
      {/* [3-2] */}
      {name==="선영표" && <div>환영합니다</div>}

      <hr/>

      {/* [3-3] */}
      <p className = "score">점수 :{score} / 등급 : {grade}등급 </p>

      
    </>
  )
}

export default App
