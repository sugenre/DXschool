use sujung;

show tables;


-- SELECT 구문 실행: 트랜잭션과 아무런 연관성이 없음
SELECT * FROM DEPT;

-- DEPT 테이블에 데이터를 1개 삽입
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(50, '회계', '서울');

SELECT * FROM DEPT;

-- 철회 : SAVE POINT를 입력하지 않으면 트랜잭션 시작 전으로 복구
ROLLBACK;

SELECT * FROM DEPT;





-- ---------------
-- 삽입 - 트랜잭션이 생성  
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(50, '회계', '서울');


-- DEPT 테이블의 모든 내용을 가진 DEPTCOPY 테이블을 생성
-- DDL(CREATE, DROP, ALTER, TRUNCATE, RENAME), DCL(GRANT, REVOLE)를 수행하면 AUTO COMMIT
-- COMMIT 수행 : 트랜잭션은 변경 내용을 반영하고 종료
CREATE TABLE DEPTCOPY
AS
SELECT * FROM DEPT;

-- 철회
ROLLBACK;


SELECT *
FROM DEPT;




-- SAVEPOINT 사용법
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(60, '회계', '서울');
SAVEPOINT SV1;

INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(70, '회계', '서울');
SAVEPOINT SV2;

INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(80, '회계', '서울');

SELECT * FROM DEPT;

-- SV1을 생성한 지점으로 이동
ROLLBACK TO SV1;
-- COMMIT, DDL 을 수행하지 않아서 쓰기 LOCK이 걸림
SELECT * FROM DEPT;


COMMIT ;








-- 일반적인 JOIN 방법을 이용해서 JOB이 CLERK인 데이터의 정보를 조회
SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO AND JOB = 'CLERK';

-- INLINE VIEW를 이용한 JOIN
-- WHERE 절의 조건을 먼저 써서 메모리 부담을 줄임
-- FROM 절에 조건을 사용해서 만드는 것 - INLINE VIEW
SELECT *
FROM (SELECT * FROM EMP WHERE JOB = 'CLERK') TEMP, DEPT
WHERE TEMP.DEPTNO = DEPT.DEPTNO;

SHOW TABLES;

SELECT *
FROM DEPT;



-- EMP 테이블에서 EMPNO, ENAME, SAL, COMM 만으로 구성된 뷰를 생성
CREATE VIEW KIM
AS 
SELECT EMPNO,ENAME, SAL, COMM 
FROM EMP;


-- VIEW는 테이블 처럼 사용
-- 가려진 정보만 제공
SELECT *
FROM KIM;




-- VIEW에 DML(삽입, 삭제, 갱신) 작업은 가능한 경우도 있고 가능하지 않은 경우도 있음
DESC EMP;

-- VIEW에 데이터 삽입
-- VIEW를 만들 때 사용한 EMP 테이블에 데이터가 삽입 됨
INSERT INTO KIM(EMPNO, ENAME, SAL, COMM) VALUES(9999, 'SUJUNG', 10000, 90000);
SELECT * FROM KIM;

SELECT * FROM EMP;

-- 뷰의 구조 확인
DESC KIM;

--  뷰 삭제
DROP VIEW KIM;



-- 임시 테이블 생성 : 접속을 해재한 후 다시 연결하면 이 테이블은 소멸됨
-- 임시니까 세션 껐다 키면(연결) TABLE 사라짐
CREATE TEMPORARY TABLE TEMP(
NAME CHAR(20)
);

SELECT * FROM TEMP;






-- CTE : SQL 수행 중에만 일시적으로 메모리 공간을 할당받아서 사용하는 테이블
-- FROM 절에 쓴 서브쿼리 - INLINE VIEW
-- SELECT 구문의 결과를 일시적으로 TEMP 라는 테이블 이름을 부여해서 보관
-- 이와 유사한 작업을 INLINE VIEW를 이용해서 할 수 있을 것처럼 보이지만 
-- INLINE VIEW는 SUB QUARY보다 늦게 수행되기 때문에 INLINE VIEW  는 SUB QUARY에 사용할 수 없음
WITH TEMP AS
(SELECT NAME, SALARY, SCORE FROM tStaff WHERE DEPART = '영업부' AND GENDER= '남')
SELECT * FROM TEMP WHERE salary  >= (SELECT AVG(SALARY) FROM TEMP);


-- usertbl 테이블 존재 여부 확인
SHOW TABLES;

DESC usertbl;

SELECT *
FROM usertbl;







-- PROCEDURE 실습
DROP PROCEDURE myproc;

-- DELIMITER 는 프로시저 종료를 알리기 위한 기호를 설정하는 것인데 2개로 만드는 이유는
-- 하나 짜리로 만들면 데이터로 사용되는 것과 혼동이 올 수 있어서임
-- DBEAVER에서 수행할 때는 SQL 스크립트 실행으로 실행해야함
DELIMITER //
CREATE  PROCEDURE myproc(vuserid char(15), vname varchar(20), vbirthday int(11),
vaddr char (100), vmobile char(11), vmdate date)
        BEGIN
        	 INSERT INTO usertbl
        	 VALUES(vuserid, vname, vbirthday, vaddr, vmobile, vmdate);
        END//        	 
DELIMITER ;
      
        
CALL myproc('MANSIK', '정만식', 1974, '목포', '01011111111', '1974-12-11');

SELECT *
FROM usertbl;











-- 트리거를 수행하기 위한 샘플 테이블 생성
CREATE  TABLE EMP01(
    EMPNO INT PRIMARY KEY,
    ENAME VARCHAR(30) NOT NULL,
    JOB VARCHAR(100)
    );
    
CREATE TABLE SAL01(
    SALNO INT PRIMARY KEY AUTO_INCREMENT,
    SAL FLOAT(7,2),
    EMPNO INT REFERENCES EMP01(EMPNO) ON DELETE CASCADE
    );  
    
   
SHOW TABLES;
   




DROP TRIGER trg_01;

 -- EMP01 테이블에 데이터를 추가하면 DAL01테이블에 데이터가 자동으로 추가되는 트리거
DELIMITER //
CREATE TRIGER trg_01
AFTER INSERT ON EMP01
FOR EACH ROW  -- 여러번 반복
BEGIN 
	INSERT INTO SAL01(SAL, EMPNO) VALUES(1000, NEW.EMPNO); -- 새로운 값은 NEW 있던 값은 OLD
END//
DELIMITER ;

INSERT INTO EMP01 VALUES(0, '수정', '프로그래머');


SELECT *
FROM EMP01;


SELECT *
FROM SAL01;




-- 데이터 베이스 사용을 설정
use sujung;
show tables;
-- 테이블 구조 확인
desc DEPT;

SELECT *
FROM DEPT;


DESC tStaff;



-- 파일을 저장할 수 있는 테이블
CREATE TABLE BLOBTABLE(
	filename VARCHAR(100),
	filecontent longblob
);

DESC BLOBTABLE;

SELECT * FROM BLOBTABLE;


