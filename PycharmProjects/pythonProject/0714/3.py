#응답 코드가 200인 데이터의 개수 세기
import collections

cnt = 0
with open('./log.txt') as f:
    # 줄 단위로 읽기
    for line in f:

        #print(line)

        #읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()

        if ar[8] == '200':
            #개수를 셀 때 아래 코드를 입력하면 됨
            cnt = cnt + 1
print("200dml rotn:", cnt)





#IP 별 접속 획수 세기 - 첫번째 항목이 IP
#그룹 -> dict or counter
ipCount = {}
with open('./0714/log.txt') as f:
    # 줄 단위로 읽기
    for line in f:

        #읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        #ar[0] - IP
        #ar[0]을 key로 해서 ar[0]의 값에 1을 더하기
        ipCount[ar[0]] = ipCount.get(ar[0], 0) + 1

for ip in ipCount:
    print(ip, ipCount[ip])






#ip별 트래픽 합계
#마지막 항복이 트래픽

# . 의 이유 알아보기
ipTraffic = {}
with open('./log.txt') as f:

    # 줄 단위로 읽기
    for line in f:
    # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        try:
            ipTraffic[ar[0]] = ipTraffic.get(ar[0], 0) + int(ar[9])
        except Exception as e:
            print(e)

            # try except 쓰기 싫으면 -을 0으로 바꿔서 해결하기

for ip in ipTraffic:
    print(ip, ":", ipTraffic[ip])


import os
print(os.getcwd())
os.chdir('0714')


from collections import Counter