#접속
import redis

#Connection Pool을 이용한 접속
import time
redis_pool = redis.ConnectionPool(host='localhost', port=6379,
                                  max_connections=4)

with redis.StrictRedis(host='localhost', port=6379) as conn:
    #만료 시간 설정 가능
    conn.set("name", "sujung", 10) #만료시간 10초
    #만료 시간 확인
    print(conn.ttl("name"))

    conn.set("song", "노래")
    conn.expire("song", 10) #데이터 만료시간을 10초 설정
    print(conn.get("song"))
    time.sleep(15)
    print(conn.get("song")) #20초 후에 데이터를 가져오므로 데이터가 없어서 None




    #리스트에 데이터 저장
    conn.lpush("album", "gennesis")
    conn.rpush("album", "exodus")

    for album in conn.lrange("album", 0, 10):
        print(album)