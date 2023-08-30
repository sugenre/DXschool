import sys
import pymysql

try:
    #데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='sujung', user='root', passwd='wnddkd', charset ='utf8')
    print(con)

    #SQL 실행 객체 샐성
    cursor = con.cursor()
    #SQL 실행 -값을 직접 SQL에 작성

    cursor.execute("select * from DEPT where LOC = %s", ('신안'))


    #검색 결과 중 하나의 데이터를 읽어오는 것
    #여러 개의 데이터를 가져오는 경우는 데이터가 없는 경우
    #빈 튜플을 리턴
    record = cursor.fetchall()
    #여러 개를 리턴하는 함수를 호출해서 데이터가 없다는 사실을 확인하는 방법
    # 데이터의 개수가 0인지 확인
    if len(record) == 0:
        print("검색된 데이터가 없음")
    else:
        for attr in record:
            print(attr)

    #원본에 반영
    con.commit()

except:
    print("예외발생:", sys.exc_info())

finally:
    if con != None:
        con.close()




import sys
import pymysql

try:
    #데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='sujung', user='root', passwd='wnddkd', charset ='utf8')
    print(con)

    #SQL 실행 객체 샐성
    cursor = con.cursor()


    #삽입할 이미지 파일의 내용 읽기
    f = open('C:/Users/user/PycharmProjects/pythonProject/0720/newjeans.jpg', 'rb')
    newjeans = f.read()
    f.close()

    #데이터 삽입
    cursor.execute("INSERT INTO BLOBTABLE VALUES(%s, %s)",
                   ("newjeans.jpg", newjeans))

    #원본에 반영
    con.commit()

except:
    print("예외발생:", sys.exc_info())

finally:
    if con != None:
        con.close()







# 파일 불러오기
import sys
import pymysql

try:
    #데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='sujung', user='root', passwd='wnddkd', charset ='utf8')
    print(con)

    #SQL 실행 객체 샐성
    cursor = con.cursor()


    #데이터 읽어오기
    cursor.execute("SELECT * FROM BLOBTABLE")
    data = cursor.fetchone()
    #두번째 데이터가 blob 이므로 두번째 데이터를 파일로 변경
    print(data[0]) #파일명
    #파일을 쓰기 모드로 생성
    f = open(data[0], 'wb')
    #읽은 데이터를 파일에 기록
    f.write(data[1])
    f.close()

    #원본에 반영
    con.commit()

except:
    print("예외발생:", sys.exc_info())

finally:
    if con != None:
        con.close()
