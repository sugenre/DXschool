#접속
import redis

#Connection Pool을 이용한 접속
redis_pool = redis.ConnectionPool(host='localhost', port=6379,
                                  max_connections=4)

with redis.StrictRedis(host='localhost', port=6379) as conn:
    #문자열 저장
    conn.set("name", "제네시스")
    #문자열 가져오기
    data = conn.get("name")

    print(data)
    print(data.decode('utf-8')) #인코딩 결과가 출력됨
