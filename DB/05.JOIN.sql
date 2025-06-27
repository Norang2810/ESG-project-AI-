--CHAPTER 05 . JOIN

--JOIN 이란?
--여러 테이블에서 필요한 데이터를 한번에 가져오는 기술이다.

--RDBMS(관계형 데이터베이스) => Relationship Database Management System

--Primary key(pk)와 Foreign Key(fk) 관계로 이루어진 데이터 베이스다.

--직원테이블로부터 직원의 아이디,이름,부서ID 정보를 가져와서 출력한 것
SELECT EMPLOYEE_ID,FIRST_NAME,DEPARTMENT_ID,JOB_ID
FROM EMPLOYEES;

SELECT * FROM
DEPARTMENTS;

--직원 테이블에서 직원ID,FIRST_NAME,부서ID,부서테이블에 부서명 출력

SELECT EMPLOYEES.EMPLOYEE_ID
    ,EMPLOYEES.FIRST_NAME
    ,EMPLOYEES.DEPARTMENT_ID
    ,DEPARTMENTS.DEPARTMENT_NAME -->해당 테이블의 컬럼명을 조회
FROM EMPLOYEES, DEPARTMENTS -- 직원테이블과 부서테이블을 조인하겠다.
WHERE EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
ORDER BY EMPLOYEES.EMPLOYEE_ID ASC;
-- 조인조건 : 조인할 테이블에서 서로 같은 값을 가지는 컬럼으로 조인 조건절 작성


--[조인 프로세스]
-- 1.조인할 대상 테이블의 정보를 확인
-- 2.FROM : ,(컴마)를 기준으로 조인할 테이블을 작성
-- 3.WHER : 조인 조건이 되는 "특정 컬럼"을 확인하며 "조인조건절"을 작성
-- 조인조건이 되는 특정 컬럼 : 조인할 테이블 간의 같은 값을 가진 컬럼이다!
--> 조인은 대부분 PK와 FK 관계로 되어진다. 단 다 그런것은 아니다.
--> 같은 값을 가지는 컬럼이면 의미있는 조인이 가능하다.
-- 4.SELECT : .(경로)를  작성하여 해당 테이블의 컬럼 정보를 작성


SELECT * FROM 수강생정보;
SELECT * FROM 성적표;

-- 공통 칼럼명 => 학생ID
--수강생정보테이블에 학생ID ,학생이름,성적표 테이블의 과목과 성적
SELECT 수강생정보.학생ID,수강생정보.학생이름,성적표.과목,성적표.성적
FROM  수강생정보,성적표
WHERE 수강생정보.학생ID = 성적표.학생ID;


SELECT EMPLOYEE_ID, FIRST_NAME,SALARY,JOB_ID
FROM EMPLOYEES;


--직원ID,이름,급여,직업ID,JOB_TITLE
--조인할 테이블의 정보 : EMPLOYEES,JOBS

SELECT * FROM JOBS;
SELECT * FROM EMPLOYEES;


SELECT E.EMPLOYEE_ID,E.FIRST_NAME,E.SALARY,J.JOB_TITLE
FROM EMPLOYEES E , JOBS J
WHERE E.JOB_ID = J.JOB_ID
ORDER BY E.EMPLOYEE_ID ASC;


--FROM 절에 별칭을 사용한다
--AS라는 키워드는 사용 못한다.
--FROM절에 테이블에 별칭을 주기 위해선 공백으로 별칭을 설정한다.
--FROM절에 테이블에 별칭을 설정하였으면 이후 실행되는 절에도 반드시 별칭으로 사용해야한다.

--등가 조인사용 방법
--SELECT 테이블1.컬럼명, 테이블2.컬럼명
--FROM 테이블1 , 테이블2 -->조인하겠다.
--WHERE 테이블1.컬럼명 = 테이블2.컬럼명 ; ->조인조건절 작성

--등가조인은 Oracle에서만 사용가능한 조건절.
--INNER JOIN은 모든 데이터베이스 사용가능한 조건절. 


--[INNER JOIN 사용방법]
--SELECT 테이블1.컬럼명 , 테이블2.컬럼명
--FROM 테이블1 INNER JOIN 테이블2 --> 조인하겠다
--ON (테이블1.컬럼명 = 테이블2.컬럼명) --> 조인조건 작성
--WHERE 일반 조건절 ;

--JOB_ID가 IT_PROG 에 해당하는 직원들만 조회하시오.
SELECT E.EMPLOYEE_ID,E.FIRST_NAME,E.SALARY,J.JOB_TITLE
FROM EMPLOYEES E , JOBS J
WHERE E.JOB_ID = J.JOB_ID
AND E.JOB_ID = 'IT_PROG'
ORDER BY E.EMPLOYEE_ID ASC;

--INNER JOIN으로 바꾸기
SELECT E.EMPLOYEE_ID,E.FIRST_NAME,E.SALARY,J.JOB_TITLE
FROM EMPLOYEES E INNER JOIN  JOBS J
ON (E.JOB_ID = J.JOB_ID)
ORDER BY E.EMPLOYEE_ID ASC;






SELECT DEPARTMENT_ID,DEPARTMENT_NAME,LOCATION_ID
FROM DEPARTMENTS;


SELECT * FROM LOCATIONS;


--부서ID,부서명,위치ID,STREET_ADDRESS,CITY
--조인할 테이블의 정보 : DEPARTMENTS,LOCATIONS
--등가조인 --
SELECT d.department_id,d.department_name,d.location_id,l.street_address,l.city
FROM DEPARTMENTS D,LOCATIONS L
WHERE D.LOCATION_ID = L.LOCATION_ID;

--INNER JOIN--
SELECT d.department_id,d.department_name,d.location_id,l.street_address,l.city
FROM DEPARTMENTS D INNER JOIN LOCATIONS L
ON (d.location_id = l.location_id);





--부서ID,부서명,매니저ID,부서장(FIRST_NAME)출력
--조인할 테이블의 정보 : DEPARTMENTS,EMPLOYEES



SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D, EMPLOYEES E
WHERE  E.DEPARTMENT_ID = D.DEPARTMENT_ID;

--INNER JOIN 으로 작성


SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D INNER JOIN EMPLOYEES E
ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID);

-- LEFT OUTER JOIN 을 사용
--오라클 문법 조인시 : 조인 조건절 반대인 오른쪽 컬럼에 (+) 기호 작성
SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D LEFT OUTER JOIN EMPLOYEES E
ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID)
ORDER BY E.DEPARTMENT_ID ASC;

--오라클 문법으로 LEFT OUTER JOIN 사용
SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D , EMPLOYEES E
WHERE D.MANAGER_ID = E.EMPLOYEE_ID(+)
ORDER BY E.DEPARTMENT_ID ASC;

--RIGHT OUTER JOIN 사용
--오라클 문법 조인시 : 조인 조건절 반대인 왼쪽 컬럼에 (+) 기호 작성
SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D RIGHT OUTER JOIN EMPLOYEES E
ON (D.MANAGER_ID = E.EMPLOYEE_ID);

--오라클문법에서 RIGHT OUTER JOIN 사용
SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D , EMPLOYEES E
WHERE D.MANAGER_ID(+) = E.EMPLOYEE_ID
ORDER BY E.DEPARTMENT_ID;


--FULL OUTER JOIN 사용
--오라클 문법 조인시 : 오라클 문법에서는 지원 X
SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,D.MANAGER_ID,E.FIRST_NAME
FROM DEPARTMENTS D FULL OUTER JOIN EMPLOYEES E
ON (D.MANAGER_ID = E.EMPLOYEE_ID);

