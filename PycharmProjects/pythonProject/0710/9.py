# 오후 강의

#예제 1
def commonConcern1() :
    print("공통 관심 사항_1")

def commonConcern2() :
    print("공통 관심 사항_2")
def businessLogic():
    print("업무 로직")

def transaction():
    commonConcern1()
    businessLogic()
    commonConcern2()


#예제 2

# func = businesslogic
def deco(func):
    print("공통관심사항")
    func()

#이제부터 business Logic 이라는 함수를 호출하면 deco라는 함수를 수행함
#deco에게 매개변수로 businessLogic이라는 함수가 전달됨
#개발자가 작성한 코드 대신에 다른 코드를 불러내는 방식을 프록시 패턴이라고 함
@deco
def businessLogic():
    print("업무 로직")

businessLogic()





# 예제 2
"""
def businessLogic():
    print("업무 로직")

businessLogic()
"""

#고객의 니즈가 변경
#업무 로직와는 관계가 없는 로깅을 출력하는 코드를 추가하기를 원하는 방향으로 변경
#유지보수 과정이나 업무 로직과 관련이 없는 코드ㅡㄹ 추가하거나 삭제하는 경ㅇ우
#업무 로직을 직접 수정하는 것은 예상치 못한 결과를 만들어낼 수 있음
#이런 경우에는 ㅇ버무 로직은 손을대지 않고 가능하도록

def decorator(func):
    func()
    print("로깅")

@decoretor
def businessLogic():
    print("업부로직")

businessLogic()






#decorator 예제
import time
def clock(func):
    #decorator가 적용된 함수가 호출되면 수행될 실제 수행
    def clocked(*args):
        start = time.time()

        # 업무 로직 함수를 호출
        result = func(*args)

        end = time.time()
        elapsed = end - start #함수의 수행 시간
        print("수행시간:", elapsed)
        #매개변수 확인
        print("매개변수:", args)
        #리턴값
        print("리턴값:", result)

        return result
    return clocked
@functools.lru_cache()  #똑같은 함수 계산 X -> 속도가 빨라짐
@clock
#피보나치 수열을 구해주는 함수
#첫번째 와 두번째는 무조건 1
#세번째 부터는 이전 2개의 항의 합
def fibanacci(n):
    if n == 1 or n == 2 :
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)

print(fibanacci(5))





#oop 예제 1
class Student
    #인스턴스가 있어야만 호출되는 메서드

    def disp(self):
        print("인스턴스 생성")

#인스턴스 생성
student = Student()
#메서드 호출 - Bound 호출
student.disp()
Stusent.disp()
#메서드 호출 - UnBound 호출
Student.disp(student)





def setName(self, name):
    self.name = name #self.name은 인스턴스의 속성으로 만들어짐

#인스턴스 생성

stu = Student()
stu.setName("파이터")
print(stu.name)

stu.score = 94 #인스턴스에 score이라는 속성이 있으면 수정이고 없으면 생성
print(stu.score)






#class 생성 예제
class Student:
    class data = "클래스의 속성"

student =Student()
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

student.class_Data = "인스턴스를 이용해서 클래스 데이터 수정"
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근





#is 연산자 예제
class Student:
    class_data = "클래스의 속성"

#인스턴스 생성해서 대입
stu1 =Student()
#인스턴스 생성해서 대입
stu2 =Student()
#stu1의 데이터를 대입 :stu1이 참조하고 있는 데이터의 참조를 stu3가 참조함

# 2개의 인스턴스가 동일한지 여부를 확인
print(stu1 == stu2)#내부의 데이터가 같은지 확인 (True가 나올 수도 있음)
print(stu2 is stu2) #id가 같은지 확인




#접근자 메서드 예제

class Student:
    def setName(selfself):
        return self.name

    def setName(selfself, name):
        self.name = name

    def getScore(selfself):
        return self.score

    def setScore(self, score):
        self.score = score






stu1 = student()
#setter를 이용한 속성 생성과 설정
stu1.setName("아담")
stu1.setScore(98)
#getter를 이용한 속성 사용
print(stu1.getName())
print(stu1.getScore())
#최근에 등장한 IDE는 대부분 getter와 setter를 만드는 유틸을 제공함