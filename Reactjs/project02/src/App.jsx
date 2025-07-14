import './App.css'
// 3.컴포넌트 불러오기
import Menu from '../component/Menu.jsx'
import Myteam from '../component/Myteam.jsx'
import MyState from '../component/MyState.jsx'

function App() {

  return (
    // <>
    //   {/* 이름 : 아메리카노 , 가격 : 4100원 */}
    //   {/* props : 컴포넌트끼리의 데이터 전달 방법 
    //         -->속성값을 통해서 데이터를 전달할수있다.
    //   */}
    //   <Menu  mName='아메리카노' price ='4100'></Menu>
    //   {/* 이름 : 카페라떼 , 가격 : 4600원 */}   
    //   <Menu mName = '카페라떼' price = '5000'></Menu>
    // </>


    // <>
    //   <Myteam dept="교육운영부" dName="선영표"></Myteam>
    //   <Myteam dept="전략기획팀" dName="강예진"></Myteam>
    //   <Myteam dept="홍보팀" dName="임보미"></Myteam>
    //   <Myteam dept="기획팀" dName="최영화"></Myteam>
    // </>

    <>
    <MyState></MyState>
    </>
  )
}

export default App
