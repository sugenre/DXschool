#reduce는 2개 받아서 계산해서 리턴

from functools import reduce

result = reduce(lambda x, y : x*y,[1, 2, 3, 4])
print(result)