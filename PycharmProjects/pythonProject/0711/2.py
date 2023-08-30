#예제 1
class Sup:

    def superMethod(selfself):
        print("상위 클래스의 메서드")

#Sup 클래스를 상속받는 Sub 클래스
class Sub(Sup):

    def subMethod(self):
        print("하위 클래스의 메서드")

#Sub의 인스턴스를 생성해서 필요한 메서드 호출
s = Sub()
s.subMethod()
s.superMethod() #Sub 클래스에는 없지만 Sup를 상속 받았기 때문에 호출 가능



#예제 2
class Sup:

    def __init__(self):
        self.name = "noname"

        def superMethod(self):
            print("하위 클래스의 메서드")

#Sup 클래스를 상속받는 Sub 클래스
class Sub(Sup):

    #하위 클래스에서 __init__을 생성하면 상위 클래스의 __init__을 호출하지 앟은
    #하위 클래스에 __init__을 만들 때는 상위 크래스의 __init__을 호출해주어야함
    def __init__(self):
        super().__init__()
        self.score = 80

    def subMethod(self):
        print("하위 클래스의 메서드")

#Sub의 인스턴스를 생성해서 필요한 메서드 호출
s = Sub()
s.subMethod()
s.superMethod() #Sub 클래스에는 없지만 Sup를 상속 받았기 때문에 호출 가능
print(s.name)




#예제 3
class Sup:
        def Method(self):
            print("상위 클래스의 메서드")

# Sup 클래스를 상속받는 Sub 클래스
class Sub(Sup):
    #상위 클래스에 존재하는 메서드를 하위 클래스에서 다시 정의 - Overriding
    #목적은 기능 확장

    def Method(self):
        super().Method() #상위 클래스의 메서드 호출
        print("하위 클래스의 메서드")


# Sub의 인스턴스를 생성해서 필요한 메서드 호출
s = Sub()
s.Method()




#에제 4
import abc

class AbstractClass(metaclass=abc.ABCMeta):
    #추상 메서드 - 내용이 없는 메서드로 하위 클래스에서 구현해서 사용해야함
    @abc.abstractmethod
    def method(self):
        pass

class Sub(AbstractClass):
    def __init__(self):
    print("인스턴스 생성")

    #추상 클래스를 상속받는 경우 추상 메서드를 반드시 implementation 해주어야함
    #만들어주지 않으면 에러
    def method(self):
        print("추상 메서드 구현")

#추상 클래스는 인스턴스를 만들 수 없어서 에러
#instance = AbstractClass()

instance = Sub()




#예제 5
import sys
print(sys.modules) #사용 가능한 모듈 확인
print(sys.path) #모듈을 찾는 위치 확인

#모듈을 찾는 위치를 추가하고자 하면 sys.path.append("찾는 위치")



#예제 6
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,7))
plt.boxplot(([100, 87, 29, 76, 88],[20,30, 30, 10000, 20]))
plt.grid()
plt.show()
plt.savefig("graph.png")