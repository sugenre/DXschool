ar = [ " HEllo", "Adam", "123"]

def f(x):
    if len (x) >3:
        return x[0:3] + "..."
    return x

temp = list(map(f,ar))
print(temp)

#문제 1) : lambda로 바꾸기
# 문제 2) : ㄱ이나 o으로 시작하는 것 찾기 ->ㄱ보다 크거나 같고 ㄴ보다 작거나 같은

ar = ["김좌진", "안중근", "윤봉길", None]
#결측치 여부 확인
print(None in ar)

def f1(x):
    return x != None
ar =list(filter(f1,ar))
print(ar)


#이름이 3자 이상인 데이터만 추출
def f(x) :
    return len(x)>=3
result0 = list(filter(f1, ar))
result = list(filter(f, result0))
print(result)