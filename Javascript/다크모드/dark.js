
// 실습 : 버튼을 클릭했을때 ,화면의 배경색은 검은색으로 ,글자색은 흰색으로 변경

function changeMode() {
    // 대화 : 만약에 body태그가 class가 noramal이면 class를 dark로 바꿔라
    // 그렇지 않다면 class를 normal로 바꿔라.
    if (document.getElementById("content").className == "normal") {
        document.getElementById("content").className = "dark"
        // 버튼의 글자가 "일반모드 바꾸기" 로 변경
        document.getElementById("btn").innerText = "일반모드 바꾸기"
    } else {
        document.getElementById("content").className = "normal"
        // 버튼의 글자가 "다크모드 바꾸기" 로 변경
        document.getElementById("btn").innerText = "다크모드 바꾸기"
    }
}




document.getElementById("btn").addEventListener("click", changeMode);
