-- 데이터 베이스
use sujung;

show tables;

-- 현재 유저 확인
SELECT USER();

-- 현재 사용 중인 데이터베이스 확인
SELECT DATABASE()

-- My SQL 은 매개변수가 없는 함수는 이름만으로 수행 가능

-- EMP 테이블에서 ENAME고 COMM을 조회
SELECT ENAME, SAL, COMM
FROM EMP;

-- EMP 테이블에서 ENAME고 COMM 그리고 SAL +COMM 을 조회
-- NULL 과 연산을 하면 결과는 NULL
SELECT ENAME, SAL, COMM, SAL+COMM AS 수령액
FROM EMP; -- COMM값이 NULL이면 


-- EMP 테이블에서 ENAME고 COMM 그리고 SAL +COMM 을 조회
-- 원래 NULL 과 연산을 하면 결과는 NULL
-- COMM 값이 NULL이면 0을 리턴
SELECT ENAME, SAL, COMM, SAL + IFNULL(COMM, 0) AS 수령액
FROM EMP;

-- COALESCE 예제
-- COMM이 NULL이 아니면 COMM 을, COMM이 NULL이고 SAL이 NULL이 아니면 SAL을 리턴
SELECT COALESCE (COMM, SAL)
FROM EMP;


-- 차이 보기 아래 세개
-- EMP 테이블에서 EMPNO가 NULL이 아닌 데이터의 개수를 조회
SELECT COUNT(EMPNO)
FROM EMP;


-- COMM이 NULL이 아닌 데이터의 개수를 조회
SELECT COUNT(COMM)
FROM EMP;

-- EMP 테이블의 데이터 개수를 조회 : 모든 컬럼이 NULL이 아닌 데이터 개수 조회
SELECT COUNT(*) AS 개수
FROM EMP;

-- EMP 테이블에서 SAL의 평균 구하기
SELECT AVG(SAL)
FROM EMP;

-- EMP테이블에서 COMM의 평균 구하기
-- COMM은 4개의 데이터가 NULL이 아니고 10 개의 데이터는 NULL
SELECT AVG(COMM)
FROM EMP;

SELECT SUM(COMM)/COUNT(*)
FROM EMP;

-- 위 두개의 결과는 다름 NULL 값 처리 방법 때문에 **다시 보기

-- COMM이 NULL인 경우는 0으로 해서 평균을 계산
SELECT AVG(IFNULL(COMM, 0))
FROM EMP;

-- **복습 필요
-- ENAME 테이블에서 ENAME 과 데이터 개수를 조회 - 에러
SELECT ENAME, COUNT(*)
FROM EMP;

-- EMP 테이블에서 DEPTNO 별로 DEPTNO, ENAME, SAL의 평균 조회 : 에러
-- GROUP BY 가 있는 경우 GROUP BY 절에 없는 컬럼이나 연산식을 조회하면 행의 개수가 맞지 않아서 에러
SELECT DEPTNO, ENAME, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

-- tCity 테이블에서 region 별 popu의 합계를 조회
SELECT region, SUM(popu) 
FROM tCity
GROUP BY region;

-- 2개 이상의 컬럼으로 그룹화가 가능
-- tStaff 테이블에서 depart, gender 별로 데이터 개수를 조회
-- 두개 이상의 데이터를 그룹화 할 땐 ORDER BY를 사용해서 정렬해주는게 좋음
SELECT depart, gender, COUNT(*) 
FROM tStaff 
GROUP BY depart, gender
ORDER BY depart;

-- ** ?
-- EMP 테이블에서 DEPTNO가 5번 이상 나오는 경우 DEPTNO와 SAL의 평균 조회
SELECT DEPTNO, COUNT(*)
FROM EMP
GROUP BY DEPTNO; 

-- ?
-- 이 경우는 그룹화 되기 전에 그룹 함수를 사용해서 에러
SELECT DEPTNO, AVG(SAL)
FROM EMP
WHERE COUNT(DEPTNO) > 5 
GROUP BY DEPTNO; 

-- 위 아래 비교하기
-- 그룹 함수를 이욯나 조건은 HAVING 절에 기재해야 함 
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING COUNT(DEPTNO) >= 5;


-- tStaff 테이블에서 depart 별로 salary 평균이 340 이 넘는 부서의 depart와 salary의 평균을 조회
SELECT depart, AVG(salary)
FROM tStaff
GROUP BY depart
HAVING AVG(salary) >= 340;


-- ** 아래 두개 비교
-- tStaff 테이블에서 depart 가 인사과나 영업부인 데이터의 depart 와 salary의 최대값을 조회
SELECT depart, MAX(salary)
FROM tStaff
GROUP BY depart 
HAVING depart IN ('인사과', '영업부'); -- IN 대신에 OR을 사용해도 됨
 

-- WHERE나 HAVING은 필터링 하는 것인데 이것은 GROUP BY하기 전에 처리하는 것이 좋음
-- 집계 함수를 쓸 때만 HAVING에서 걸러내는 것
-- 집계 함수를 사용하지 않아도 되므로 WHERE에 조건을 작성하는 것이 좋음
SELECT depart, MAX(salary)
FROM tStaff
WHERE depart IN ('인사과', '영업부'); -- IN 대신에 OR을 사용해도 됨
GROUP BY depart


-- EMP 테이블에서 sal이 많은 순서부터 일련번호를 부여해서 ENAME과 SAL을 조회
SELECT ENAME, SAL
FROM EMP
ORDER BY SAL;   -- 기본 오름차순 정렬 

-- 아래 세개의 차이
-- 여기서 순위를 지정해주고 싶으면 SELECT 구문에 입력
SELECT ROW_NUMBER() OVER( ORDER BY SAL DESC) AS '금여가 많은 순서', ENAME, SAL
FROM EMP
ORDER BY SAL DESC;

-- 여기서 순위를 지정해주고 싶으면 SELECT 구문에 입력
-- EMP 테이블에서 sal이 많은 순서부터 일련번호를 부여해서 ENAME과 SAL을 조회
-- EMP 테이블에서 SAL 이 많은 순서부터 도일한 값은 동일한 순위를 부여해서 ENAME과 SAL을 조회
SELECT DENSE_RANK() OVER( ORDER BY SAL DESC) AS '금여가 많은 순서', ENAME, SAL
FROM EMP
ORDER BY SAL DESC;

-- 동일한 순위가 있으면 다음 순위는 건너뜀
SELECT RANK() OVER( ORDER BY SAL DESC) AS '금여가 많은 순서', ENAME, SAL
FROM EMP;


-- 그룹으로 분할 : 3등분
SELECT NTILE(3) OVER(ORDER BY SAL DESC) AS '금여가 많은 순서', ENAME, SAL
FROM EMP;


-- EMP 테이블에서 DEPTNO 별로 sal이 많은 순서부터 동일한 값은 동일한 순위를 부여해서 ENAME과 SAL을 조회
SELECT DEPTNO, DENSE_RANK() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP
ORDER BY DEPTNO;



-- LEAD 와 LAG의 차이
-- EMP 테이블에서 SAL의 내림차순으로 정렬한 다음 데이터 와의 SAL의 차이르 알고자 하는 경우
SELECT ENAME, SAL, SAL - (LEAD(SAL,1) OVER (ORDER BY SAL DESC)) AS ' 급여 차이'
FROM EMP
ORDER BY SAL DESC;  -- 보통 ORDER BY 함수는 PARTITION 이 있을 때 사용함

SELECT ENAME, SAL, SAL - (LAG(SAL,1) OVER (ORDER BY SAL DESC)) AS ' 급여 차이'
FROM EMP
ORDER BY SAL DESC;


-- EMP 테이블에서 SAL의 내림차순으로 정렬한 다음 데이터 와의 SAL의 차이르 알고자 하는 경우
SELECT ENAME, SAL, SAL - (FIRST_VALUE(SAL) OVER (ORDER BY SAL DESC)) AS ' 급여 차이'
FROM EMP
ORDER BY SAL DESC;


-- 급여의 누적 백분율
SELECT ENAME, SAL, CUME_DIST() OVER(ORDER BY SAL DESC) * 100 AS "누적 백분율"
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에는 JOB과 DEPTNO 와 SAL 항목이 존재함
--  JOB별 그리고 DEPTNO 별 SAL의 합계를 구하고자 함
SELECT JOB, DEPTNO, SUM(SAL)
FROM EMP
GROUP BY JOB, DEPTNO;

-- PIVOT 이용
SELECT JOB,
    SUM(IF(DEPTNO=10, SAL, 0)) AS '10',
    SUM(IF(DEPTNO=20, SAL, 0)) AS '20',
    SUM(IF(DEPTNO=30, SAL, 0)) AS '30',
    SUM(SAL) AS '합계'
FROM EMP  
GROUP BY JOB;

-- JSON 출력
SELECT JSON_OBJECT("ename", ENAME, "sal", SAL) AS "JSON 조회"
FROM EMP;


-- EMP 테이블에서 DEPTNO를 조회 : 10,20, 30
SELECT DISTINCT DEPTNO
FROM EMP;

-- DEPT 테이블에서 DEPTNO를 조회 : 10, 20, 30, 40
SELECT DEPTNO
FROM DEPT;

-- EMP 테이블과 DEPT 테이블에서 DEPTNO의 합집합 : 중복 제거
SELECT DEPTNO
FROM EMP
UNION -- UNION ALL 쓰면 중복된 데이터도 다 나옴
SELECT DEPTNO
FROM DEPT;




-- EMP 테이블과 DEPT 테이블에서 DEPTNO의 교집합 : 중복 제거
SELECT DEPTNO
FROM EMP
INTERSECT
SELECT DEPTNO
FROM DEPT;


-- DEPT 테이블에는 존재하지만 EMP 테이블에는 존재하지 않는 DEPTNO
SELECT DEPTNO
FROM DEPT
EXCEPT
SELECT DEPTNO
FROM EMP;


-- 테이블 구조 확인
EMP 테이블 구조 확인: DESC EMP;
EMPNO - 사원번호, 기본키
ENAME - 사원이름
JOB - 직문 
MGR - 관리자 사원번호
HIREDATE - 입사일
SAL - 급여
COMM - 보너스
DEPTNO - 부서 번호


-- ENMAE이 MILLER인 사원의 DNAME을 조회
SELECT DEPTNO
FROM EMP 
WHERE ENAME = 'MILLER';

SELECT DNAME
FROM DEPT 
WHERE DEPTNO = 10;


-- SUB QUARY를 이용한 해결
-- 알고자하는 사실이 하나면 쿼리 하나를 호출하는 것을 선호함
-- 괄호 안의 SUB QUARY를 먼저 수해해서 10을 찾아오고 그 값을 이용해서 DNAME을 조회
SELECT DNAME
FROM DEPT 
WHERE DEPTNO = (SELECT DEPTNO
                FROM EMP 
                WHERE ENAME = 'MILLER');

               
-- EMP 테이블에서 SAL의 평균보다 더 많은 SAL을 받는 직원의 ENAME과 SAL을 조회
SELECT ENAME, SAL 
FROM EMP 
WHERE SAL > (SELECT AVG(SAL) 
             FROM EMP);

            
            
-- EMP 테이블에서 ENAME이 MILLER인 사원과 동일한 직무(JOB)을 가진 사원의 ENAME과 JOB을 조회
-- MILLER는 제외
SELECT ENAME, JOB
FROM EMP
WHERE JOB = (SELECT JOB FROM EMP WHERE ENAME = "MILLER") AND ENAME != 'MILLER';


-- EMP 테이블에서 DEPT 테이블의 LOC가 DALLAS인 사원의 ENAME과 SAL을 조회
SELECT ENAME, SAL
FROM EMP 
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS');


-- EMP 테이블에서 DEPTNO별 SAL의 최대값과 동일한 SAL을 갖는 사원의 ENAME, EMPNO, SAL을 조회

-- 이 구문으니 에러 : 서브 쿼리의 결과가 3개라서 =로 비교가 불가능
SELECT EMPNO, ENAME, SAL 
FROM EMP
WHERE SAL = ( SELECT MAX(SAL)
              FROM EMP
              GROUP BY DEPTNO); 
             
-- 서브 쿼리의 결과가 2개 이상인 경우는 그 중의 하나의 값과 일치하면 됨
SELECT EMPNO, ENAME, SAL 
FROM EMP
WHERE SAL IN(SELECT MAX(SAL)
              FROM EMP
              GROUP BY DEPTNO);

-- EMP 테이블에서 DEPTNO가 30인 데이터들의 SAL보다 큰 데이터의 ENAME과 SAL을 조회
-- DEPTNO가 30인 데이터는 2개 이상이므로 >로는 비교가 불가능
-- 모든 데이터보다 커야하는 경우는 ALL을 같이 사용
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > ALL(SELECT SAL
              FROM EMP
              WHERE DEPTNO = 30);
             
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > (SELECT MAX(SAL)
              FROM EMP
              WHERE DEPTNO = 30);
             
             
-- 데이터 중 1개보다만 크면 되는 경우는 ANY를 같이 사용    
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > ANY(SELECT SAL
              FROM EMP
              WHERE DEPTNO = 30);
             
             
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > (SELECT MIN(SAL)
              FROM EMP
              WHERE DEPTNO = 30);

             
 -- EMP 테이블에서 SAL이 2000이 SAL이 2000이 넘는 데이터가 있으면 ENAME과 SAL을 조회
 -- 2000이 넘는 데이터가 존재하므로 모든 데이터를 조회
SELECT ENAME, SAL
FROM EMP
WHERE EXISTS(SELECT 1 FROM EMP WHERE SAL > 2000);



-- Catesian Produnt(교차 곱)
-- FROM 절에 테이블 이름이 2개 이상이고 JOIN 조건이 없는 경우
-- EMP 테이블은 8열 14행, DEPT 테이블은 3열 4행
-- 결과는 11열 56행

SELECT *
FROM EMP, DEPT;

-- EQUI JOIN
-- FROM 절에 테이블 이름이 2개 이상이고 WHERE 절에 2개 테이블의 공통된 컬럼의 값이 같다라는 조인 조건이 있는 경우
SELECT *
FROM EMP, DEPT 
WHERE EMP.DEPTNO = DEPT.DEPTNO;

-- 한 쪽 테이블에만 존재하는 컬럼을 출력할때는 컬럼 이름만 기재해도 됨
SELECT ENAME, DNAME, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

-- 양쪽 테이블에 모두 존재하는 컬럼의 경우는 앞에 테이블 이름을 명시해야함
-- 테이블 이름을 명시하지 않으면 이름이 애매 모호하다고 에러가 발생
SELECT ENAME, DEPTNO, DNAME, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

-- 앞에 누구의 DEPTNO인지 명시해두면 됨
SELECT ENAME, EMP.DEPTNO, DNAME, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;


-- 테이블 이름에 새로운 이름 부여
SELECT ENAME, e.DEPTNO, DNAME, LOC
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;

-- FROM에서 부여하는 것은 새로운 이름을 부여하는 것으로 기존 이름은 이제 사용할 수 없음
SELECT ENAME, e.DEPTNO, DNAME, LOC
FROM EMP e, DEPT d
WHERE e.DEPTNO = DEPT.DEPTNO; -- 에러

-- HASH JOIN
SELECT /*+ ORDERED USE_HASH(E) */   -- E는 별명임
ENAME, e.DEPTNO, DNAME, LOC
FROM DEPT d, EMP e
WHERE d.DEPTNO = e.DEPTNO;

-- NON EQUI JOIN
-- EMP 테이블의 SAL은 급여임
-- SALGRADE 테이블의 LOSAL은 최저 급여 그리고 HOSAL은 최대 급여이고 GEADE는 등급
-- EMP 테이블에서 ENAME 과 SAL 을 조회하고 SAL에 해당하느 GEADE를 조회하고자 하는 경우

SELECT ENAME, SAL, GRADE
FROM EMP, SALGRADE
WHERE SAL BETWEEN LOSAL AND HISAL;

-- EMP 테이블에서 ENAME이 MILLER인 사원의 관리자 이름을 조회
-- EMP 테이블에서 ENAME과 관리자 ENAME을 조회
-- 앞의 EMP는 현재 종업원이 되고 뒤의 EMP는 관리자
-- 종업원의 관리자 사원번호와 일치하는 관리자의 사원번호를 찾아서 이름을 조회
SELECT employee.ename, manager.ename
FROM EMP employee, EMP manager
WHERE employee.mgr = manager.empno;


-- ANSI CROSS JOIN 
SELECT *
FROM EMP CROSS JOIN DEPT;


-- EMP 테이블과 DEPT 테이블의 INNER JOIN
SELECT *
FROM EMP INNER JOIN DEPT 
ON EMP.DEPTNO = DEPT.DEPTNO;

-- 2개의 컬럼 이름이 같은 경우 USING 사용이 가능
SELECT *
FROM EMP INNER JOIN DEPT 
USING (DEPTNO); 

-- 2개의 컬럼 이름이 같은 경우 NATURAL JOIN 사용가능
-- 동일한 컬럼을 1번만 출력
SELECT *
FROM EMP NATURAL JOIN DEPT; 

-- OUTER JOIN
SELECT DISTINCT DEPTNO
FROM EMP;

SELECT DEPTNO
FROM DEPT ;


-- EMP에 존재하는 모든 DEPTNO가 JOIN에 참여
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- DEPT의 존재하는 모든 DEPTNO가 JOIN에 참여
-- DEPT에는 존재하지만 EMP에는 존재하지 않는 40이 JOIN에 참여
-- 이 경우 40 은 자신의 데이터 말고는 NULL
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- MY SQL은 FULL OUTER JOIN을 지원하지 않음
SELECT *
FROM EMP FULL OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;  -- 에러



-- FULL OUTER JOIN을 UNION으로 해결한 것
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;
UNION
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;





