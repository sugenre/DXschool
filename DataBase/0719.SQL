-- 데이터 베이스 사용 설정
use sujung;

-- 테이블 생성
-- 테이블 이름은 contact
-- 속성
   -- num은 정수이고 일련번호 그리고 기본키
   -- name은 한글 7자까지 저장하고 글자 수는 변경되지 않는다고 가정
   -- address는 한글 100자까지 저장하고 글자 수의 변경이 자주 발생
   -- tel 은 숫자로된 문자열 11자리이고 글자 수의 변경은 발생하지 않음
   -- email은 영문 100자 이내이고 글자 수의 변경이 자주 발생
   -- birtday 는 날짜만 저장
   -- 주로 조회를 하고 일련번호는 1부터 시작하고 인코딩은 utf8

CREATE TABLE contact(
    num INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(21),
    address TEXT,    
    tel VARCHAR(11),
    email CHAR(100),
    birthday DATE
    )ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET =utf8;
   
   
  -- contact 테이블에 age 컬럼을 정수 자료형으로 추가
  ALTER TABLE contact 
  ADD age INTEGER;
 
 -- contact 테이블 구조 확인
 DESC contact;
  

-- contact 테이블에서 age 컬럼 삭제
ALTER TABLE contact 
DROP age;

DESC contact;




-- g. 컬럼 수정
-- contact 테이블에서 tel 컬럼의 이름을 phone으로 자료형은 정수로 수정
ALTER TABLE contact 
CHANGE tel phone INTEGER;

DESC contact;



-- contact 테이블 삭제
DROP TABLE contact;

SHOW TABLES;


-- DEPT 테이블은 EMP 테이블에서 DEPTNO 컬럼을 참조하므로 삭제가 안됨
DROP TABLE DEPT;


  
-- NOT NULL 제약 조건 설정 
CREATE TABLE tNullable(
    name CHAR(10) NOT NULL,
    age INTEGER
);

INSERT INTO tNullable(name, age) VALUES("sujung", 23);
INSERT INTO tNullable(age) VALUES(44);

DROP TABLE tNullable;


-- 기본값 설정 
CREATE TABLE tDefault(
    name CHAR(10) NOT NULL,
    age INTEGER DEFAULT 0
);

INSERT INTO tDefault(name, age) VALUES("sujung", 23);
-- 기본값이 설정된 컬럼을 제외하고 입력하면 그 컬럼에는 기본값이 삽입됨
INSERT INTO tDefault(name) VALUES("adam");

-- 데이터 확인
SELECT *
from tDefault;


-- name, gender(성별 - 남 또는 여), age(나이는 양수)를 속성으로 갖는 
-- 테이블 생성
CREATE table tCheck(
    name CHAR(10) NOT NULL,
    gender CHAR(3) CHECK(gender IN('남', '여')),
    age INT check(age >= 0)
   );
INSERT INTO tCheck(name, gender, age) VALUES('김좌진', '남', 53);
-- age가 음수라서 에러
INSERT INTO tCheck(name, gender, age) VALUES('홍범도', '남', -23);
-- gender가 여자라서 에러
INSERT INTO tCheck(name, gender, age) VALUES('유관순', '여자', 32);

SELECT *
FROM tCheck;

-- 기본키 설정
CREATE TABLE tPK1(
    name CHAR(10) PRIMARY KEY,
    age INT
    );
    
-- 기본키 설정: 제약조건 이름과 함께 생성
CREATE TABLE tPK2(
    name CHAR(10) 
    age INT,
    CONSTRAINT PK_tPK2 PRIMARY KEY(name)
);
    
   
-- 2개의 컬럼으로 기본키 설정: 테이블을 생성할 때 PRIMARY KEY는 한번만 사용 가능   
CREATE TABLE tPK3(
    name CHAR(10) PRIMARY KEY 
    age INT,PRIMARY KEY
);
    
CREATE TABLE tPK3(
    name CHAR(10)
    age INT,
    CONSTRAINT PK_tPK3 PRIMARY KEY(name, age)
);


INSERT  INTO tPK1(name, age) VALUES('sujung', 25);
-- 기본키인 name의 값이 같아서 삽입 실패
INSERT  INTO tPK1(name, age) VALUES('sujung', 56);
-- 기본키인 name의 값이 NULL 삽입 실패
INSERT  INTO tPK1(age) VALUES(25);



CREATE TABLE tUnique(
name CHAR(10),
age INT UNIQUE,
CONSTRAINT tUnique PRIMARY KEY(name)
);

INSERT  INTO tUnique(name, age) VALUES('sujung', 25);
-- age가 중복되서 삽입 실패
INSERT  INTO tUnique(name, age) VALUES('jung', 25);
-- unique는 null은 삽입 가능
-- null은 중복 체크 대상이 아니라서 삽입 가능하고 중복도 가능
INSERT  INTO tUnique(name) VALUES('jung');
INSERT  INTO tUnique(name) VALUES('hunter');

SELECT *
FROM tUnique;

-- 외래키를 지정하지 않는 2개의 테이블

-- 직원 테이블
CREATE TABLE tEmployee(
    name CHAR(10) PRIMARY KEY,
    salary INT NOT NULL,
    addr VARCHAR(30) NOT NULL);
    
INSERT INTO tEmployee VALUES('김수정', 630, '대구');
INSERT INTO tEmployee VALUES('정만식', 870, '목포');
INSERT INTO tEmployee VALUES('이국종', 230, '광주');

SELECT *
FROM tEmployee;



-- 프로젝트 테이블
-- employee는 프로젝트에 참여한 직원 이름
CREATE TABLE tProject(
    projectid INT PRIMARY KEY,
    emploee CHAR(10) NOT NULL,
    project VARCHAR(30) not null,
    cost INT
);

INSERT INTO tProject VALUES(1,'김수정', '웹 서비스', 3000);
-- 조이는 tProject 테이블에 없는 이름인데도 삽입이 가능 
INSERT INTO tProject VALUES(2,'조이', 'Microservice 구축', 10000);

SELECT *
from tProject;

-- 기존 테이블 삭제
DROP TABLE tEmployee;
DROP TABLE tProject;


-- 테이블 존재 여부 확인
show TABLES;



-- 외래키 설정 - 직원 과 프로젝트의 관계는 1:N
-- 직원 테이블
CREATE TABLE tEmployee(
    name CHAR(10) PRIMARY KEY,
    salary INT NOT NULL,
    addr VARCHAR(30) NOT NULL);
    
INSERT INTO tEmployee VALUES('김수정', 630, '대구');
INSERT INTO tEmployee VALUES('정만식', 870, '목포');
INSERT INTO tEmployee VALUES('이국종', 230, '광주');

SELECT *
from tEmployee;



CREATE TABLE tProject(
    projectid INT PRIMARY KEY,
    emploee CHAR(10) NOT NULL REFERENCES tEmployee(name), 
    project VARCHAR(30) NOT NULL,
    cost INT
);



CREATE TABLE tProject(
    projectid INT PRIMARY KEY,
    employee CHAR(10), 
    project VARCHAR(30) NOT NULL,
    cost INT,
    CONSTRAINT FK-emp FOREIGN KEY (employee) REFERENCES tEmployee(name)
);    
    
INSERT INTO tProject VALUES(1,'김수정', '웹 서비스', 3000);
-- 조이는 tProject 테이블에 없는 이름인데도 삽입이 가능 
INSERT INTO tProject VALUES(2,'조이', 'Microservice 구축', 10000);
-- tEmployee 테이블의 데이터를삭제
DELETE FROM tEmployee WHERE name = '정만식';
-- 아이린은 tProject 테이블에서 참조하고 있기 때문에 삭제가 불가능
DELETE FROM tEmployee WHERE name = '김수정;'
-- tEmployee 테이블 삭제 불가능
DROP TABLE tEmployee;


-- 실습을 위해서 기존 테이블 삭제
DROP TABLE tProject;
DROP TABLE tEmployee;
DROP TABLE tEmploee;
SHOW TABLES;


-- 옵션과 함께 외래키 설정 - 직원 과 프로젝트의 관계는 1:N
-- 직원 테이블
CREATE TABLE tEmployee(
    name CHAR(10) PRIMARY KEY,
    salary INT NOT NULL,
    addr VARCHAR(30) NOT NULL);
    
INSERT INTO tEmployee VALUES('아이린', 630, '대구');
INSERT INTO tEmployee VALUES('정만식', 870, '목포');
INSERT INTO tEmployee VALUES('이국종', 230, '광주');

SELECT *
from tEmployee;

















DROP TABLE tProject;
-- tEmployee 테이블의 name이 수정되거나 삭제될 때 같이 수정되거나 삭제됨
-- set null이면 null로 변하고 cascade면 같이 변함
CREATE TABLE tProject(
    projectid INT PRIMARY KEY,
    employee CHAR(10), 
    project VARCHAR(30) NOT NULL,
    cost INT,
    CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name)
        ON DELETE CASCADE ON UPDATE CASCADE
); 

INSERT INTO tProject VALUES(1,'아이린', '웹 서비스', 3000);

SELECT *
from tEmployee;


-- tEmp  테이블에서 아이린을 배주현을 수정
UPDATE tEmployee SET name = '배주현' WHERE name = '아이린';

SELECT *
from tEmployee;

SELECT *
from tProject;



-- tEmployee 테이블에서 배주현을 삭제 : tProject 에서도 연쇄 삭제가 발생
DELETE FROM tEmployee WHERE name = '배주현';

SELECT *
from tEmployee;

SELECT *
from tProject;





-- 일련번호 사용
CREATE TABLE BOARD(
num INT AUTO_INCREMENT PRIMARY KEY,
title CHAR(100),
content TEXT
);


-- 자동으로 1,2 순서대로 삽입
INSERT INTO BOARD(title, content) values("제목1", "제목2");
INSERT INTO BOARD(title, content) values("제목2", "제목3");
SELECT * FROM BOARD;

-- 2번 데이터 삭제
DELETE FROM BOARD WHERE num = 2;
INSERT INTO BOARD(title, content) values("제목3", "내용3");
-- 3번으로 삽입
SELECT * FROM BOARD;


-- AUTO_INCREMENT 값도 직접 삽입이 가능
INSERT INTO BOARD(num, title, content) VALUES(200, "제목", "내용");
-- 다음 숫자인 201로 삽입됨
INSERT INTO BOARD(title, content) VALUES("제목", "내용");
-- 중간에 삽입됨
INSERT INTO BOARD(num, title, content) VALUES(5, "제목", "내용");
SELECT * FROM BOARD;


-- 일련번호 초기화
ALTER TABLE BOARD AUTO_INCREMENT = 1000;
INSERT INTO BOARD (title, content) VALUES("아", "야");
SELECT * FROM BOARD;




-- 제약조건 조회
SELECT *
FROM information_schema.table_constraints;


-- 데이터 삽입을 위해서 테이블 구조를 확인
DESC tCity;

-- 컬럼 이름을 나열해서 데이터 삽입
INSERT INTO tCity (name, area, popu, metro, region)
VALUES('평택', 200, 130, 'n', '경기');

-- 모든 컬럼의 값을 순서대로 입력하는 경우는 컬럼 이름 생략이 가능
INSERT INTO tCity 
VALUES('목포', 20, 13, 'n', '경기');

-- NOT NULL이 설정된 컬럼을 제외하고는 생략하고 삽입 가능
INSERT INTO tCity(name, area, region)
VALUES('대전', 20, '서울');

SELECT *
FROM tCity;

-- 여러개 한꺼번에 삽입하는 방법 - 나열
INSERT INTO tCity(name, area, metro, region)
VALUES('대전', 20, 'y', '서울'), ('마산', 87, 'n', '경상');



SELECT * 
FROM tCity;

-- tCity 테이블에서 name이 대전인 데이터 삭제
DELETE FROM tCity WHERE name = '대전';

-- tCity 테이블에서 name이 마산인 데이터의 POPU를 40으로 수정
UPDATE tCity SET popu = 40 WHERE name = '마산';
