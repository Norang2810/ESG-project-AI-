/* [테이블을 삭제하는 방법]
  DROP [테이블명];
  
  수강생정보 테이블과 성적표 테이블 삭제
  
  테이블의 정보를 확인하는방법
  1.DESC[테이블명];
  2.해당 테이블을 마우스로 드래그 후 SHIFT +F4
*/

-- 참조되고있는 제약조건을 강제로 옵션을 줘서 테이블을 삭제.
--DROP TABLE [테이블명] CASCADE CONSTRAINT;
desc 수강생정보;

--수강생정보 테이블 삭제
DROP TABLE 수강생정보 CASCADE CONSTRAINT;

--성적표 테이블 삭제
DROP TABLE 성적표 CASCADE CONSTRAINT;



CREATE TABLE 수강생정보 (
학생ID   VARCHAR2(9) PRIMARY KEY , 
학생이름  VARCHAR2(50) NOT NULL , 
소속반    VARCHAR2(5) 
); 

CREATE TABLE 성적표 (
학생ID VARCHAR2(9),
과목  VARCHAR2(30),
성적  NUMBER,
CONSTRAINT PK_성적표 PRIMARY KEY(학생ID , 과목),
CONSTRAINT FK_성적표 FOREIGN KEY(학생ID) REFERENCES 수강생정보(학생ID)
) ;


SELECT * FROM 성적표;


--DML(Data Manipulation Language) : 데이터 조작어

/* 데이터 조작어란 데이터베이스에 저장된 데이터를 입력 수정 삭제하는 언어
    DML의 유형 -- 셀인업디
    SELECT :데이터 조회 
    INSERT :데이터 추가
    UPDATE :데이터 수정
    DELETE :데이터 삭제
*/

SELECT * FROM 수강생정보;

INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD1','박진우','B');
INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD2','지누','B');
INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD3','Heyjinu','B');
INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD4','ParkJinwoo','B');
INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD5','Jinwoo','B');
INSERT INTO 수강생정보 (학생ID,학생이름,소속반)VALUES ('SMHRD6','Jinu','B');


/*
    INSERT INTO에 컬럼 리스트를 생략하는 경우
    데이터베이스는 해당 테이블의 컬럼리스트를 다 작성된걸로 간주하고
    VALUES에는 모든 컬럼에 대한 실제 값을 순서와 자료형에 맞춰서 작성해야한다.
*/


--UPDATE [테이블명]
--SET [변경할 내용]
--WHERE [데이터를 변경할 대상 행을 선별하기 위한 조건식]

UPDATE 수강생정보
SET 소속반 = 'C'
WHERE 학생이름 = 'Heyjinu';

UPDATE 수강생정보
SET 소속반 = 'C'
WHERE 학생이름 LIKE '%oo';

/*
    PK의 특징 : NOT NULL + UNIQUE (유일성과 최소성 만족)
    UPDATE나 DELETE를 할때 조건절에는 PK로 되어있는 칼럼을 기준을 삼는것이 올바르다!
*/

COMMIT ; --영구 저장하는 명령어

INSERT INTO 수강생정보 VALUES ('SMHRD1' , '조준용' , 'A') ;
INSERT INTO 수강생정보 VALUES ('SMHRD2' , '박수현' , 'A')  ;
INSERT INTO 수강생정보 VALUES ('SMHRD3' , '박병관' , 'B')  ;
INSERT INTO 수강생정보 VALUES ('SMHRD4' , '이명훈' , 'B')  ;
INSERT INTO 수강생정보 VALUES ('SMHRD5' , '나예호' , 'B') ;
INSERT INTO 수강생정보 VALUES ('SMHRD6' , '선영표' , 'C')  ;
INSERT INTO 수강생정보 VALUES ('SMHRD7' , '최영화' , 'C')  ;
INSERT INTO 수강생정보 VALUES ('SMHRD8' , '송찬호' , 'C')  ;
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


SELECT * FROM 성적표;

/*
    UPDATE실습
    성적표 테이블에서 SMHRD6인 학생의 JAVA의 성적을 100점을 업데이트 해주기
*/


UPDATE 성적표
SET 성적 = 100
WHERE 학생ID = 'SMHRD6' AND 과목 = 'JAVA';



DELETE FROM 성적표
WHERE 학생ID = 'SMHRD1';

SELECT * FROM 성적표;

ROLLBACK ; --되돌리는 명령어

--TCL 명령어
--트랜잭션 제어어
--트랜잭션이란 업무를 처리하기위한 최소 수행 단위를 뜻한다.
--데이터베이스의 상태를 변화시키기 위해서 수행하는 최소 수행단위

/*
    [TCL의 명령어]
    COMMIT      : 데이터베이스에 영구 저장하는 명령어
    ROLLBACK    : 트랜잭션을 취소, 마지막 COMMIT시점까지만 복구가 가능
    SAVEPOINT   : 중간 저장하는 명령어, 하나의 트랜잭션을 작게 분할하여 저장하는 기능을 수행한다.
    
    
    DCL -데이터 제어어
    데이터 제어어로서 데이터베이스에 접근하거나 객체에 권한을 주는 등의 역할을 하는 언어
    
    DCL 명령어 종류
    GRANT   :권한을 부여하는 명령어
    REVOKE  :권한을 회수하는 명령어
    ROLE    :권한을 묶어서 부여할때 사용하는 명령어
    
    CREATE USER [계정명]
    IDENTIFIED BY [비밀번호];
    
    
    [시스템 권한 부여방법]
    GRANT [시스템권한]
    TO [계정(사용자)];
    
    [시스템 권한 회수 방법]
    REVOKE [시스템 권한]
    FROM [계정(사용자)];
    
    [SQL COMMAND LINE에서 권한을 주었다.]
    GRANT CONNECT , RESOURCE TO [사용자];
    
    ROLE : 여러 권한을 한번에 부여하기 위해 사용하는 명령어
    CREATE SESSION : 접속을 할수 있는 권한
    GRANT CREATE SEESION TO [사용자명];
    
    ROLE의 종료
    CONNECT  ->데이터베이스에 접속에 필요한 권한
    RESOURCE ->테이블,시퀀스 등 객체를 생성할수 있는 권한
*/