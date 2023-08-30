
from decimal import Decimal
#실수 표현의 한계때문에 2개 연산의 결과가 다르게 나옴
print(123.456 + (0.23456 + 1.2337))
print((123.456 + 0.23456) + 1.2337)

#실수를 문자열로 만들어서 DEcimal 모듈을 이용하면 정확한 계산을 수행
print(Decimal('123.456') + (Decimal('0.23456') + Decimal('1.2334')))
print((Decimal('123.456') + Decimal('0.23456')) + Decimal('1.2334'))


#random 예제
import random
"""
import time
li = ["오미크론", "다크스펙터", "라투"]
for i in range(10):
    time.sleep(1)
    print(li[random.randint(0, len(li)-1)])
"""
#공백을 기준으로 정수 6개를 받아서 list로 만든 후 정렬을 수행
i = input("1부터 45까지의 정수를 공백을 구분해서 6개 입력하세요.")
x = i.split(" ")
lotto = list(map(lambda e : int(e), x))
lotto.sort()
print(lotto)

#1부터 45까지 숫자에서 6개를 랜덤하게 추출해서 입력한 숫자와 일치하는지 확인해서
#몇번 추출했는지 확인
ar = range(1, 46)
cnt = 0
while True:
    k = random.sample(ar,6)
    k.sort()
    cnt = cnt + 1
    if lotto == k:
        break

print(cnt)

"""
li1 = [ 1, 2, 3]
li2 = [ 1, 2, 3]

print(li1 == li2)
"""