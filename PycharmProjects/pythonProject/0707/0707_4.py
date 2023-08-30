#Hello 3번 출력
def display():
    for i in range(3):
        print("Hello")
display()

#Hello 출력
print("Hello")
dsiplay()
print(display) #함수 이름은 함수를 저장한 곳의 참조

li = [ 10, 8, 9]

##
def intAddWithInt(a, b):
    return a+b
# --

#함수가 종료되고 다시 함수를 호출하기 때문에
#어느 한 순간에 하나의 스택만 존재
#result =inAddWithInt(100,300)
#x = intAddWithInt(result, 600)
#print(x)
#--

#함수의 수행이 종료되기 전에다른 함수를 호출하기 때무에
#

def intOpWithInt(a, b):
    return a+b, a-b
#튜플로 만들어서 리턴
#튜플 전체를 하나의 변수로 받기

t = intOpWithInt(100,200)

print(t)

#튜플을 분해해서 받기

add, sub = intOpWithInt(100, 200)

print(add, sub)

#--
#정수 2개를 담아서 결과를 정수로 리턴하는 함수
def add(a : int, b : int) -> int:   #UML표기법
    return a + b
print(add(300,100))