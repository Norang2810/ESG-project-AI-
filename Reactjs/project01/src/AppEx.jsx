import './App.css'


function AppEx() {

    // 1.사용자에게 이름을 입력받는다(userName)
    let name = prompt('이름을 입력하세요.')
    // 2.현재날짜를 가지고 온다(today)
    let today = new Date()
    console.log('현재날짜 :', today.toLocaleDateString())
    // 3.현재 날짜에서 월만 빼오기(month)
    console.log('월 :', today.getMonth() + 1)
    let month = today.getMonth() + 1
    // 4.조건에 따라 계절을 정의하기(season)
    let season = ""

    if (parseInt(month / 3) === 1) {
        season = '봄'
    } else if (parseInt(month / 3) === 2) {
        season = '여름'
    } else if (parseInt(month / 3) === 3) {
        season = '가을'
    } else {
        season = '겨울'
    }
    console.log(name, month, season)
    // 3~5 : 봄  / 6~8 :여름 / 9~11 :가을 / 12 ~2 :겨울
    // 5.test용으로 console창에 1~4번까지의 결과 출력
    // [결과창]
    // h1 => 2025.07.13
    // 수평선 hr
    // h3 = > 000님 지금은 여름입니다. 좋은 하루보내세요.
    




    return (
        <>
            <div>
                <h1>{today.toLocaleDateString()}</h1>
                <hr />
                <h3>{name}님 지금은 {season}입니다. 좋은하루보내세요.</h3>
            </div>
        </>
    )
}



export default AppEx