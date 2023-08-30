ar = [10, 20, 30]
#try-except를 빼면 0을 입력했을 때 예외가 발생함
#예외 구간을 except로 빼내 준 것
try:
    su = int(input("나눌 수를 입력하세요:"))

    i = 0
    j = len(ar)
    while i < j:
        if su == 1:
            raise ValueError("강제로 예외 발생")
        # 아래 것보다 위에 것이 더 효율적임
        # 아래 것은 함수 호출을 여러번 해야하는데 위에는 한번만
        # while i< len(ar):
        assert su != 2,'su는 2이면 안됩니다.'
        print(ar[i] / su)
        i = i + 1

except ValueError as e:
    print("잘못된 데이터를 입력했습니다.")
    print(e)

except ZeroDivisionError as e:
    print("0으로 나눌 수는 없습니다.")
    print(e)
else :
    print("예외가 발생하지 않은 경우 수행할 내용")
finally:
    print("무조건 수행하는 문장")




import os
#print(os.getcwd()) #상대 결로를 설정할 때 기준 경로

try:
    file = open('./0714/test.txt', 'w', encoding='utf-8')

    file.write('abcd') #문자열 기록
    lines = ["김좌진", "홍범도", "김구"]
    file.writelines(lines)

    #줄 단위 읽기
    for line in file:
        print(line)
        print()

except Exception as e:
    print("파일 처리 중 예외 발생")

finally:
    file.close()



import csv
data = []
with open('./0714/test.csv', 'r', encoding='utf-8') as file:
    #줄 단위로 읽어서 list를 만들어주는 reader 객체를 생성
    #읽고 싶으면 reader 기록하고 싶으면 writer
    rdr = csv.reader(file)
    for line in rdr:
        data.append(line)

print(data)




#텍스트 아일을 읽어서 list로 변환
#마지막 데이터에는 \n이 추가됨
#마지막 데이터는 \n을제거해주어야 함
import csv
data = []
with open('./0714/test.bin', 'wb') as file:
    file.write("안녕하세요".encode())
with open('./0714/test.bin', 'rb') as file:
    content = file.read()
    print(content.decode())
##오류



import csv
data = []
with open('./0714/test.csv', 'w', encoding='utf-8') as file:
    wr = csv.writer(file)
    wr.writerow(['김수정', '백은하'])





class DTO:

    def __init__(self, num=0, name="이름 없음"):
        #__private이라 안에서만 쓸 수 있음
        self.__num = num
        self.__name = name

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def name(self):
        return self.__name

    @name.setter
    def num(self, name):
        self.__name = name

    #인스턴스를 print 함수에 대입했을 때 호출되는 메서드 - 오버라이딩
    #출력을 편리하게 하기 위해서 재정의 - 디버깅 목적
    def __str__(self):
        return str(self.__num) + ":" + self.__name

#파일에 기록할 데이터 생성
dto1 = DTO(1, "sujung")
dto2 = DTO(2, "은하")

data = [dto1, dto2]


import pickle
try:
    with open("./0714/data.data", "wb") as f:
        #f에 data를 Serializable
        pickle.dump(data, f)
except Exception as e:
    print(e)







import zipfile
#압축할 파일 목록 생성
filelist = ["./data/data.data", "./data/test.bin"]

#파일 목록을 순회하면서 압축
with zipfile.ZipFile(',/0714/test.zip','w') as myzip:
    for temp in filelist:
        myzip.write(temp)



zipfile.ZipFile("./0714/test.zip").extractall()