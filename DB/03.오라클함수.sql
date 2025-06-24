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

