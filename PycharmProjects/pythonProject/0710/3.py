#2번 응용
# 문제 1) : lambda로 바꾸기

ar = ["김좌진", "안중근", "윤봉길", None]
#결측치 여부 확인
print(None in ar)

def f1(x):
    return x != None


ar =list(filter(lambda x : x != None,ar))
print(ar)



ar1 = ["김좌진", "안중근", "윤봉길"]
def f(x) :
    return len(x)>=3

result = list(filter(lambda x : len(x) >= 3, ar1))
print(result)




# 2번 응용 2

ar = ["김좌진", "안중근", "윤봉길", None]

#문자열 비교가 가능한지 확인
print("가" > "나")
print("가" < "나")

result = list (filter(lambda x : x[0] >= "아" and x[0] < "자", ar))
print(result)