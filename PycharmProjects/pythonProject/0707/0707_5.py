def collection(a, b):
    print(a)
    print(b)
collection(10, 20)
collection(*[100, 200]) # List를 분할해서 a에 100 b에 200이 대입
collection(*{"key1": 100, "key2" : 200})
#dict는 *이 1개이면 key 값이 매개변수에 전달됨
collection(**{"a": 100, "b":200})
#dic는 *이 2개이면 value 값이 매개변수에 전달됨
# 이때 key 이름과 매개변수 이름이 같아야 됨



#가변 매개변수 사용
#매개변수 개수 상관없이 대입해서 호출 가능
#함수 내부에서는 튜플
def merge(*li):
    for element in li:
        print(element)

merge(10)
merge(10, 20)
merge(10, 20, 30)


def merge(*li, name):
    for element in li:
        print(element)

merge(10, 20, 30, name="adam") #name에 adam이 대입되고 나머지는 li에 대입

#merge(10, 20, 30, ”adam”)  #이 구문은 에러
