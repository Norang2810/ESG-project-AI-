DROP TABLE 학생인적사항 ;
DROP TABLE 수강생정보 ; 
DROP TABLE 성적표 ; 

CREATE TABLE 수강생정보 (
학생ID   VARCHAR2(9) PRIMARY KEY , 
학생이름  VARCHAR2(50) NOT NULL , 
소속반    VARCHAR2(5) 
); 

CREATE TABLE 성적표 ( 
    학생ID VARCHAR2(9) , 
    과목   VARCHAR2(30) , 
    성적   NUMBER  , 
    CONSTRAINT PK_성적표 PRIMARY KEY(학생ID , 과목) , 
    CONSTRAINT FK_성적표 FOREIGN KEY(학생ID) REFERENCES 수강생정보(학생ID) 
)  ; 

INSERT INTO 수강생정보 VALUES ('SMHRD1' , '조준용' , 'A') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD2' , '박수현' , 'A') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD3' , '박병관' , 'B') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD4' , '이명훈' , 'B') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD5' , '나예호' , 'B') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD6' , '선영표' , 'C') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD7' , '최영화' , 'C') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD8' , '송찬호' , 'C') ; 
INSERT INTO 수강생정보 VALUES ('SMHRD9' , '임승환' , 'C') ; 

INSERT INTO 성적표 VALUES('SMHRD1'  ,'JAVA' , 90); 
INSERT INTO 성적표 VALUES('SMHRD1'  ,'DATABASE' , 85); 
INSERT INTO 성적표 VALUES('SMHRD1'  ,'PYTHON' , 100); 
INSERT INTO 성적표 VALUES('SMHRD2'  ,'JAVA' , 100); 
INSERT INTO 성적표 VALUES('SMHRD2'  ,'DATABASE' , 100); 
INSERT INTO 성적표 VALUES('SMHRD2'  ,'PYTHON' , 20); 
INSERT INTO 성적표 VALUES('SMHRD3'  ,'JAVA' , 100); 
INSERT INTO 성적표 VALUES('SMHRD3'  ,'DATABASE' , 100); 
INSERT INTO 성적표 VALUES('SMHRD3'  ,'PYTHON' , 20); 
INSERT INTO 성적표 VALUES('SMHRD4'  ,'JAVA' , 85); 
INSERT INTO 성적표 VALUES('SMHRD4'  ,'DATABASE' , 40); 
INSERT INTO 성적표 VALUES('SMHRD4'  ,'PYTHON' , 60); 
INSERT INTO 성적표 VALUES('SMHRD5'  ,'JAVA' , 100); 
INSERT INTO 성적표 VALUES('SMHRD5'  ,'DATABASE' , 100); 
INSERT INTO 성적표 VALUES('SMHRD5'  ,'PYTHON' , 100); 
INSERT INTO 성적표 VALUES ( 'SMHRD6' , 'JAVA' , NULL ) ; 
INSERT INTO 성적표 VALUES ( 'SMHRD6' , 'DATABASE' , NULL ) ; 
INSERT INTO 성적표 VALUES ( 'SMHRD6' , 'PYTHON' , NULL ) ; 

COMMIT;




select * from 성적표;
select * from 수강생정보;





SELECT 소속반 , COUNT(학생ID) AS "학생수"
FROM 수강생정보
GROUP BY 소속반;




--직원테이블에서 부서별 최고 급여와 최저 급여를 집계하여 출력

SELECT * FROM EMPLOYEES;

SELECT DEPARTMENT_ID, MAX(SALARY),MIN(SALARY)
FROM  EMPLOYEES
GROUP BY  DEPARTMENT_ID 
ORDER BY DEPARTMENT_ID ; 

--직원테이블에서 직업별(GROUP BY) 평균 급여를 구하시오.
--조건 : 사장님의 직업 AD_PRES인 것을 제외를 시켜라.


--직원테이블에서 부서별 평균 급여를 구하시오
--조건 : 부서가 30,50,80,100 에 해당하는 부서만 조회하시오.

select round(avg(salary),1) as "평균급여"
from employees
where department_id in (30,50,80,100)
group by department_id;



--HAVING 절 : GROUP BY절이 실행이 되고 집계가 완료된 대상을 조건을 통해 필터링하는 문법
-->집계함수에 대한 조건을 걸때 사용하는 "조건절"이다

-- HAVING절 사용하는 방법


--직원테이블에서 부서별(GROUP BY) 최고 연봉이 100000 이상인 부서만 출력.

SELECT * FROM EMPLOYEES;

SELECT  DEPARTMENT_ID, MAX(SALARY ) AS "최고 연봉"
FROM    EMPLOYEES
GROUP BY DEPARTMENT_ID;

--직업별 평균 급여를 구하시오.
--단 AD_PRES인 것을 제외하고 평균 급여가 100000 이상인 데이터만 출력

SELECT  JOB_ID , AVG(SALARY) AS "평균급여"
FROM    EMPLOYEES
where job_id != 'AD_PRES'
GROUP BY JOB_ID
HAVING AVG(SALARY) >= 10000;

--부서별 급여별 총합계를 구하시오.
--단 급여 총합계가 10000 이하인 부서만 출력하고, NULL값을 가진 부서는 출력이 되면 안된다.

SELECT department_id,SUM(SALARY) as "총합계"
FROM EMPLOYEES
WHERE DEPARTMENT_ID IS NOT NULL
GROUP BY DEPARTMENT_ID
HAVING SUM(SALARY) <= 10000;











