
function print() {
    alert("기능이 실행됐습니다!");
}
// 실행위치 : JS를 작성하는 위치는 3가지 존재
// 1)인라인 방식 = 태그 안에 직접 JS코드를 작성하는 기법
// 2)내부방식 = HTML파일 안에 <script>태그를 통해서 작성하는 기법
document.getElementById("btn3").addEventListener("click", print);