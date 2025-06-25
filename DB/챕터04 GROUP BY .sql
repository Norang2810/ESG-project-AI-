--CHAPTER 04.그룹바이 (GROUP BY)


--내장함수 : 오라클에서 미리 만들어 놓은 함수이다 > 호출해서 사용하는 함수

--내장함수의 종류
--단일행 함수 : 입력된 하나의 행당 결과가 하나씩 나오는 함수
--다중행 함수 : 여러 행을 입력받아서 하나의 결과 값으로 출력이 되는 함수
--> 다중행함수 = 집계함수


/*
    COUNT() : 지정한 데이터의 개수를 반환
    SUM() : 지정한 데이터의 합을 반환
    MAX() : 지정한 데이터 중 최대 값 반환
    MIN() : 지정한 데이터 중 최소 값 반환
    AVG() : 지정한 데이터의 평균 값 반환

    직원 테이블에서 직원 ID의 행의 갯수를 조회하시오.
*/

SELECT COUNT(EMPLOYEE_ID)
FROM EMPLOYEES;

--출력하려고 하는 컬럼의 행의 갯수가 맞지 않기 때문에 에러를 발생
/*
    다중행 함수(집계함수)의 특징
    1.집계함수는 NULL 값을 제외하는 특성을 가짐.
    2.집계함수는 GROUP BY 가 된 상태에서만 사용가능한 함수이다.
*/


select count(department_id)
from employees
group by();

/*
    직원 테이블을 하나의 그룹으로 묶은걸로 인식을 한 상태이다.
    
    count() : 지정한 데이터의 개수를 반환하는 함수
    *(아스타리스크) 사용할수있다.
    다른 집계함수는 사용할 수없다.

*/

select count(*)
from employees;

--직원 테이블에서 급여의 총 합계 구하기
select sum(salary)
from employees;


--문제1) 직원테이블에서 직원의 최대 급여와 최소 급여를 구하시오.

SELECT max(salary) as "최대급여"
        ,min (salary) as "최소급여"
FROM employees;


--문제2) 직원테이블에서 부서ID가 100인 직원의 평균 급여를 구하시오. (단, 결과값은 소수점 1의 자리까지 반올림하여 출력)


select round(avg(salary),1) as "직원의 평균 급여"
from employees
where department_id = 100;

/* [GROUP BY절 사용하는 방법]
    SELECT 조회하고자 하는 "칼럼의정보"
    FROM 데이터를 가져올 "테이블의 정보"
    WHERE 원하는 행을 선별하기위한 조건식
    GROUP BY 그룹화

*/

