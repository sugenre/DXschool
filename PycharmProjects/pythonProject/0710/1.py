#숫자 list를 가지고 제곱한 list를 생성

li =[i for i  in range (10000)] #0부터 9999까지의 숫자르 가지고 list를 생성

temp = []

for x in li :
    temp.append(x * x)

print(temp)


def f(x):
    return x*x

#li의 모든 요소에 f함수를 적용해서 변환한 결과를 tmep에 대입
#함수의 내용일 한 줄 이므로 람다로 처리
temp = list(map(lambda x : x*x, li) #map을 이용한 변환
print(temp)