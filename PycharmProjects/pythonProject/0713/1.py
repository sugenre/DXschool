problem = "GDKKDGCCGDDFDDGCCGCCGDDDGCCGDDDGCCGFFF"
#위 문자열에서 GCCG의 위치를 전부 출력
#한 번 포함되면 포함된 문자는 빼고 찾아야함
#GCCGCCG는 1번만 찾아야 함  p.64 이용




#현재 시스템의 인코딩 확인
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#문자열을 바이트 코드로 변환
print("한글".encode())
print("한글".encode().decode())

print(ord("a"), ord("한"))





import re
# : 이나 |를 , 로 치환
testStr = "apple:samsung google|kakao"

result = re.sub("[:,|]", ",", testStr)
print(result)





#email이 유효한 이메일 인지 검사
p = re.compile("^[a-zA-z0-9+-|-.]+@[a-zA-Z0-9-]+|.[a-zA-Z0-9-.]+$")

emails = ["sujung9401@naver.com", "0dong@"]

for email in emails:
    print(p.match(email) != None)




#list의 메서드 활용
li1 = ["sujung", "adam", "soccer", "11st"]
li2 = list(range(10))

#데이터 추가
li1.append("navigation")

#한 개 데이터 출력
print(li1[0])
#슬라이싱 - 범위를 가지고 추출
print(li1[0:2])

#데이터 삭제
del li1[3]

#데이터 순회
for project in li1:
    print(project)






#list의 정렬
li1 = ["sujung", "adam", "soccer", "11st"]
li1.sort()#오름차순 정렬
print(li1)
li1.sort(reverse=True) #내림차순 정렬
print(li1)

result = sorted(li1) #sorted는 정렬한 결과를 리턴
print(result)

#영문 대소문자 구분없이 정렬
li1.sort(key = str.lower) #reverse 적용 가능
print(li1)





record = ("adam", "sujung", 2) #튜플 생성
print(record)
print(record[0]) #인덱싱 가능
#record[0] = "아담" #수정불가능

#list와 tuple은  unpacking이 가능
name, job, albumCnt = record
print(albumCnt)

*etc, albumCnt = record #*을 이용하면 모두를 list로 생성
print(etc)

#swap : 2개의 데이터의 값을 치환
a = 10
b = 20

a,b = b, a
print(a,b)




#테이블 구조의 데이터 생성
data = [("sujung", "010"), ("adam", "987)"]

#이름만 출력
for row in data:
    print(row[0])

#컬럼에 이름을 사용하는 튜플
from collections import namedtuple

#자료구조 생성 - 튜플의 각 컬럼 이름 만들기
Person = namedtuple("Person", "name mobile")
persons = [Person('sujung', '010'), Person('adam', '987')]
for person in persons:
    print(person,name)




#set은 데이터의 순서와 상관없이 저장되므로 출력되는 순서는 예측할 수 없음
s = {"adam", "genesis", "exodus", "genesis"}
print(s)
s.add("numbers")
for d in s:
    print(d)




dic = {}
dic["name"] = "adam"
dic["job"] = "singer"
dic["father"] = "pms"
dic["father"] = "pjm"
print(dic)
#항목 가져오기
print(dic["job"])
print(dic.get("job", "nojob"))
#print(dic["score"]) #존재하지 않는 key를 사용하면 keyErroe 발생
print(dic.get("score", "0")) #존재하지 않는 key를 사용하면 두번째 매개변수 리턴
#순회
for key in dic:
    print(key, dic[key])







#dict를 이용한 MVC

#DTO 역할을 수행하는 클래스 생성 - 최근에는 더 권장

class DTO:
    def __init__(selfself, name="noname", tel = "전화없음"):
        self.name = name
        self.tel = tel

#데이터 목록 출력 (요즘 ver)
datas = [DTO("adam", "010"), DTO("sujung", "011")]

#이름과 전화번호 출력
for data in datas :
    print (data.name, data.tel)

#위에거 변형 (옛날 ver)
datas = [{"name":"adam", "tel":"010"}, {"name":"sujung", "tel":"011"}]
for data in datas:
    for key in data:
        print(key, ":", data[key])



#이차원 배열 대신에 dict 사용
kia = ["윤영철", "최형우"]
lg = ["켈리 ", "클럿코"]

kbo = [kia, lg] #list의 list
#list는 index를 이용해서 접근하고 dict는 key를 이용해서 접근

#enumerate는 인덱스와 데이터를 튜플로 리턴
#인덱스를 이용하면 변화에 적응이 잘안됨
for idx, baseball in enumerate(kbo):
    if idx ==0:
        print("기아", ends="\t")
    else :
        print("엘지", ends="\t")

    for player in baseball:
        print(player, end="/t")
    print()





#이차원 배열 대신에 dict 사용
kia = ["윤영철", "최형우"]
lg = ["켈리 ", "클럿코"]
hanhwa =["노시환"]

kbo = [{"team":"기아", "data":"kia"}, {"team":"엘지", "data":lg}, {"team":"한화","data":hanhwa}]

for dic in kbo:
    print(dic.get("team"),end=":")
    for plyer in dic.get("data"):
        print(plyer, end="\t")
    print()