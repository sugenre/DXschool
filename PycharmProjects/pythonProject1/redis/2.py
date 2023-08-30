#접속
import redis

#Connection Pool을 이용한 접속
import time
redis_pool = redis.ConnectionPool(host='localhost', port=6379,
                                  max_connections=4)

with redis.StrictRedis(host='localhost', port=6379) as conn:
    #리스트에 데이터 저장
    conn.lpush("album", "gennesis")
    conn.rpush("album", "exodus")

    for album in conn.lrange("album", 0, 10):
        print(album)