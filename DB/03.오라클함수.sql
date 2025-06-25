--CHAPTER 03.오라클 함수

SELECT FIRST_NAME
    ,UPPER (FIRST_NAME) AS UPPER함수활용
    ,UPPER('first_name')
    FROM EMPLOYEES;
    
    
    SELECT EMAIL
        ,LOWER(EMAIL)
        FROM EMPLOYEES;
        
--        LENGTH() : 소괄호 안에 있는 문자 데이터의 길이를 구하는 함수

SELECT 'HELLO WORLD' ,LENGTH('HELLO WORLD') AS DDD
FROM DUAL;

--DUAL테이블이란 함수 결과값 확인 용도로 사용하는 테스트용 테이블입니다.


--직원의 FIRST_NAME의 길이가 7이상인 직원의 이름(FIRST_NAME)과 급여 정보를 조회하시오.

SELECT  FIRST_NAME,SALARY ,LENGTH('FIRST_NAME')AS 직원이름길이
FROM EMPLOYEES
WHERE LENGTH(FIRST_NAME) >= 7;

--SUBSTR() :  문자열을 추출하는 함수이다.
--SUBSTR(입력값,시작위치,추출길이)

SELECT '광주인공지능사관학교 개강'
        ,SUBSTR('광주인공지능사관학교 개강',7,4) AS "사관학교"
        ,SUBSTR('광주인공지능사관학교 개강',10,2) AS "교"
        ,SUBSTR('광주인공지능사관학교 개강',1,6) AS "광주인공지능"
        ,SUBSTR('광주인공지능사관학교 개강',3)
FROM DUAL;
        
--REPLACE() : 특정 문자를 다른 문자로 바꾸어주는 함수
--REPLACE(문자열데이터,바꾸고싶은문자,바꿔야할 문자)
--바꿔야할 문자를 생략 가능 > 단 생략시 바꾸고 싶은 문자가 삭제가 된다.
SELECT REPLACE('인공지능#사관학교','#','-')
        ,REPLACE('인공지능#사관학교','#') AS "삭제"
FROM DUAL;


--[숫자형 함수]
--ROUND() : 특정 위치에서 반올림 하는 함수

SELECT ROUND(12345.56789,2) AS "반올림 된 숫자"
    ,ROUND(12345.56789) AS "강제로 반올림"
FROM DUAL;


--MOD() :숫자를 나눈 나머지 값을 구하는 함수
--(나눗셈 될 숫자, 나눌 숫자)
--홀수 ,짝수를 구분하기 위해서

SELECT MOD(123,10) AS "나머지"
        ,MOD(12,5) 
FROM DUAL;


--[날짜형 함수]
--SYSDATE : 현재 날짜와 시간을 출력해주는 함수
--입력 시 바로 출력이 되며, 현재 시간을 초 단위까지 출력이 가능하다.


SELECT SYSDATE
FROM DUAL;  
        
        
--날짜형식 세팅        
--        도구 > 환경설정 > 데이터베이스 >NLS > 날짜형식 > YYYY-MM-DD HH:24:MI:SS

--명시적 형변환 : 데이터 변환 형 함수를 사용해서 사용자가 직접 자료형을 지정 해주는 것
--TO_NUMBER() : 문자 데이터를 숫자 데이터로 변환하는 함수
--TO_NUMBER(문자열 데이터, 인식 될 숫자 형태)        
--자료형 변환 시 표현할 수있는 표현 방식
-- 9 --> 빈자리를 0으로 채움을 의미
-- 0 --> 빈자리를 0으로 채움을 의미
-- $ --> 달러($) 표시를 붙혀서 출력을 해준다.
-- L --> 지역 화폐 단위 기호를 붙혀서 출력함
-- . --> 소수점
-- , --> 천 단위의 구분 기호를 표시함


SELECT TO_NUMBER('1,000','9999') + 900 AS "숫자형 변화"
FROM DUAL;


--TO_CHAR() : 날짜,숫자 데이터를 문자 데이터로 변환 해주는 함수
--TO_CHAR(변환 할 데이터,출력 형태)

--직원 테이블에서 직원의 이름과 급여 정보를 가져온것(출력한 것)
SELECT FIRST_NAME
    ,SALARY
    ,TO_CHAR(SALARY,'L999,999') AS "문자형 단위"
FROM EMPLOYEES;


--TO_DATE() : 문자 데이터를 날짜 데이터로 변환하는 함수
--TO_DATE(문자열 데이터,인식 될 날짜 형태)

SELECT TO_DATE('20250624','YYYY/MM/DD')
FROM DUAL;

-- [NULL 처리 함수]
--NVL() / NVL2() : NULL값을 대체할 수 있는 함수

--NVL(NULL인지 여부를 검사할 데이터, NULL일 경우 반환할 데이터)
--NVL(값,NULL아닐때 나올값,NULL일때 나올값)

--직원테이블에서 보너스(COMMISSION_PCT)가 NULL일 경우 숫자 0으로 대체 해서 출력
SELECT EMPLOYEE_ID,FIRST_NAME,SALARY,COMMISSION_PCT
    ,NVL(COMMISSION_PCT,0) AS "NVL함수값"
FROM EMPLOYEES;


--직원테이블에서 직원ID,FIST_NAME,MANAGER_ID를 출력
--매니저가 있는 직원은 "직원" 로 가공하여 출력
--매니저가 없는 직원은 "대표" 로 가공하여 출력


SELECT employee_id,first_name,manager_id
    ,NVL2(MANAGER_ID,'직원','대표') AS "직무"
FROM EMPLOYEES;


--조건함수
--DECODE() : 상황에 따라 다른 데이터를 반환하는 함수
--> 검사 대상과 비교해서 지정한 값을 반환

--DECODE(검사대상이 될 데이터<기준1>,<비교값2>,<일치 할 경우 반환값3>,<일치하지않을때 반환값4>)
--직원테이블에서 직원ID,FIST_NAME,MANAGER_ID를 출력
--매니저가 있는 직원은 "직원" 로 가공하여 출력
--매니저가 없는 직원은 "대표" 로 가공하여 출력

SELECT employee_id,first_name,manager_id
        ,decode(manager_id,null,'대표','직원')
        ,decode(manager_id,100,'대표',101,'전무',102,'상무',103,'팀장','직원')
from employees;









