class Student:

    #생성자 - 인스턴스를 생성할 때 호출하는 메서드
    #보통 이 메서드에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어주는 것이 좋음
    #매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화가 가능
    #매개변수를 이용해서 초기화 할 때 매개변수에 기본값을 설정하지 않으면
    #인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야 함

    def __init__(self, name="noname"):
        # name값을 입력하면 입력한 값, 입력 X면 noname으로
        print("인스턴스 생성")
        #특정한 상수로 생성하고자하는 경우는 생성자 내부에서 직접 생성
        # self.name = "기본값"
        self.name = name


    #소멸자 - 인스턴스가 소멸될 때 호출되는 메서드
    def __del__(self):
        print("인스턴스 소멸")

    def disp(self):
        print("인스턴스 메서드")
        #만들어지기는 클래스에 만들어졌지만 인스턴스 없이는 호출할 수 없는 메서드

    #setter - 속성을 수정하거나 생성하는 메서드
    def setName(self,name):
        self.name = name #name이라는 속성이 없으면 만들어서 대입하고 존재하면 수정


    #getter - 속성의 값을 사용할 수 있도록 리턴하는 메서드
    def getName(self):
        return self.name

stu1 = Student() #인스턴스 생성
#메서드 호출
Student.disp(stu1) #클래스가 인스턴스의 메서드를 호출 - unbound호출
stu1.disp() #self레 인스턴스가 대입되서 메서드를 호출 - bound 호출


stu1.setName("sujung")
print(stu1.getName())







#예제 2

#클래스 생성
class Student:
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    #클래스 속성과 생성자를 이용한 일련번호 만들기

    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment


stu1 = Student()
print(stu1.no)
stu2 = Student()
print(stu2.no)




#예제 2

#클래스 생성
class Student:
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    #클래스 속성과 생성자를 이용한 일련번호 만들기

    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment


    def __del__(self):
        print("인스턴스 소멸")


stu1 = Student() #인스턴스가 생성되고 참조 카운트가 1이 됨
stu1 = None #참조를 가리키는 변수에 None을 대입하면 참조 카운트가 1 감소 (이거 없으면 뜨는 메세지 순서가 달라짐)
#참조 카운트가 0이면 인스턴스가 소멸됨


stu2 = Student() #참조 카운트 1
stu3 = stu2 #다른 변수에 참조를 대입하므로 참조 카운트는 1 증가 2
stu2 = None #참조 카운트가 1 줄어들어도 1 - 인스턴스는 소멸되지 않음
print("프로그램 종료")




#예제 3

#클래스 생성
class Student:
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    #클래스 속성과 생성자를 이용한 일련번호 만들기

    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment


    def __del__(self):
        print("인스턴스 소멸")

    @staticmethod
    def method():
        print("매개변수가 없는 staticmethod")

Student.method()

stu1 = Student() #인스턴스가 생성되고 참조 카운트가 1이 됨
stu1 = None #참조를 가리키는 변수에 None을 대입하면 참조 카운트가 1 감소 (이거 없으면 뜨는 메세지 순서가 달라짐)
#참조 카운트가 0이면 인스턴스가 소멸됨


stu2 = Student() #참조 카운트 1
stu3 = stu2 #다른 변수에 참조를 대입하므로 참조 카운트는 1 증가 2
stu2 = None #참조 카운트가 1 줄어들어도 1 - 인스턴스는 소멸되지 않음
print("프로그램 종료")




#예제 4
#클래스 생성

class Student()
    # name과 age 속성만 사용하도록 제한
    __slot__ = ["name", "age"]




stu1 = Student()
stu1.name = "sujung"
stu1.age = 35
stu1.job = "singer"


#예제 5

#클래스 생성
class Student:


    def __init__(self):
        self.name = "sujung"
        self.__no = 1 #속성을 만들 때 __로 시작하면 인스턴스는 속성에 직접 접근 불가


stu1 = Student()
print(stu1.name)
#__no private 변수라 안됨
#print(stu1.__no)




#예제 6

class Student

    def __init__(self, name = "noname"):
        self.__name = name #속성 이름이 __로 시작하므로 인스턴스로 접근 불가


    #접근자 메서드
    @property #getter 설정
    def name(self):
        print("name의 getter 호출")
        return self.__name

    @name.setter
    def name(self, name):
        print("name의 setter 호출")
        self.__name = name

    #프로퍼티 생성
    #name을 호출하면 getANme 메서드가 호출되고 ㅜ믇 에 값을 대입하면 setNAme 메서드가 호출됩
    name = property(fget=getName, fset=setName)


stu = Student()
#setter와 getter를 직접 호출
stu.Name("파이터")
print(stu.getName())
#property를 이용한 getter와 setter 호출
stu.name = "나이트"
print(stu.name)




#예제 7

class Student:

    def __init__(self, name="noname"):
        self.name = name


    # +연산자 오버로딩
    # 아래 두줄 없으면 print(stu1 + stu2) 코드 오류남
    def __add__(self, other):
        return self.name + other.name

    #==연산자 오버로딩

    def __eq__(self, other):
        return self.name == other.name


stu1 =Student("강진축구")
stu2 = Student("강진축구")
print(stu1 + stu2)

stu3 = stu1
print(stu1 == stu2)
print(stu1 is stu2)





#예제 8
class Student:

    def __init__(self, name="noname", count=0):
        self.name = name
        self.count = count

    def __add__(self, other):
        return self.count + other.count


stu1 = Student("사과", 3)
stu2 = Student("배", 2)
print(stu1 + stu2)