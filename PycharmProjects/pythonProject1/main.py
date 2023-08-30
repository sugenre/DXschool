# mongo db 사용을 위한 패키지를 import
from pymongo import MongoClient

#연결
conn = MongoClient('localhost', port=27017)
#print(conn)

#데이터베이스 사용 설정
db = conn.sujung #없으면 생성됨

#컬렉션 설정
#삽입이나 삭제 또는 갱신을 하게되면 결과를 리턴함
collect = db.data

result = collect.insert_one({"empno": "10001", "name":"수정", "phone": "010-3790-1999", " age":53})

print(dir(result))

result = collect.insert_many([{"empno": "10001", "name":"수정", "phone": "010-3790-1999", " age":53},
                    {"empno": "10002", "name":"철수", "phone": "010-1230-1569", " age":33},
                    {"empno": "10003", "name":"오동", "phone": "010-3000-1999", " age":63}])

#삽입 삭제 확인할 수 있도록 다음 print를 사용함
#DB에서도 확인해야함 - commit 때문에
print(result.inserted_id)



collect = db.data
#데이터 조회
#데이터 조회를 하게되면 커서를 리턴함
# 커서를 순서대로 접근하면 데이터가 dict로 접근 가능함
result = collect.find()
for temp in result:
    print(type(temp))
    print(temp.get("name", "이름없음"))

collect = db.data
#데이터 수정
#수정할 때는 set연산자가 들어가야함
collect.update_many(
    {'empno':"10001"},
    {'$set':{'name':"김수정"}}
)


# 조건 설정 후 정렬
result = collect.find({" age": {"$gt": 10}}).sort("age")
for temp in result:
    print(temp.get("name", "이름없음"))