#피보나치 수열을 재귀로 구하는 함수
#첫번째와 두번째는 1 그 이후 부터는 이전 2개 항의 합
#1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89

def fibonacci(n:int) -> int:
    if n == 1 or n== 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(10))  #55
print(fibonacci(11))  #89




##파이썬의 일급 객체 예제

def dragonkAttack():
    print("드래곤의 공격")

def tankAttack():
    print("탱크의 공격")

delegate = dragonkAttack
delegate()

delegate = tankAttack
delegate()

##고위함수 예제

def outer():
    def inner():
        print("soqn gkatn")
    return inner()

#함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출
func = outer()
func()
