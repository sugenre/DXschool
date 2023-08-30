li = list(range(10)) #0부터 9까지 숫자를 가지고 list를 생성
#li의 모든 데이터를 제곱한 list를 생성
#append or map(filiter) 함수 이용해서 만들기


help(map)
help(filter)

#1.일반 반복문을 이용하는 방법
li = list(range(10))
result = []
for i in li:
    result.append(i*i)
print(result)



#2.map함수를 이용하는 방법

result = list(map(lambda i : i*i, li))
print(result)


#3.list comprehension 이용
#[연산식 순회할 문장]

result = [ i*i for i in li]
print(result)


#for 2개 사용
li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
result = [x*y for x in li1 for y in li2]
print(result)

#for와 if를 사용 가능 - filtering
singers = ["태연", "수지", "아이유", "새벽공방"]

#글자 수가 3이상인 데이터만 추출
#아래 것이 더 빠름 (함수 X 기 때문에)
result = list(filter(lambda x : len(x) >=3, singers))
print(result)
result = [x for x in singers if len (x) >= 3 and len(x) < 4]
print(result)
#위에 것과 아래 것 같은 것으로 작용 (and, if)
result = [x for x in singers if len (x) >= 3 if len(x) < 4]
print(result)


singers = ["태연", "수지", "아이유", "새벽공방"]
#if ~else for 활용
#3글자 이상은 그대로 나머지는 _를 추가
result = [x if len(x) >= 3 else x + "_" for x in singers]
print(result)


from collections import Counter
data = ["한식", "중식", "분식", "한식", "일식","양식", "한식", "분식"]
#데이터 목록을 가지고 데이터 개수 파악
counter = Counter(data)
#dict로 변환해서 전체 데이터의 개수 파악
print(dict(counter))
#한가지 데이터 파악
print(counter["한식"])
#상위 2개만 추출
print(counter.most_common(2))





data = [("APPLE", 3), ("APPLE", 2), ("ORANGE", 3), ("MONGGO", 3), ("ORANGE", 5)]
counter = Counter()

#데이터가 등장한 횟수 구하기
#구조분해할당..
for name, count in data:
    counter[name] += count
    print(counter)

#데이터의 합계를 구해보기
counter = Counter()
for name, count in data:
    counter[name] += 1
    print(counter)




def div(x):
    return 10/x

try:
    print(div(20))
    print(div(0))
except:
#try절에서 문제가 발생하면 수행되는구문
     print("예외발생")
print("프로그램 종료")