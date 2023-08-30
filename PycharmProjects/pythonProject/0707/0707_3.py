#문제 1
#2부터 100까지 완전수의 개수
#완전수는 자신을 제외한 약수의 합이 자신과 같은 수
#6은 완전수  6의 약수 1, 2, 3, 6 6빼고 더하면 6

#for a in range (1, 101, 1)
#    if i == a:
#        print(a)
#    elif i % a == 0:
#        print(a, end = "")
cnt = 0 #완전수의 개수를 저장할 변수
for idx in range(2, 1001):
    #약수의 합을 저장할 변수
    #합계를 구할 때 무조건 0으로 초기화 하지는 않음
    hap = 1
    #2부터 자신의 수 전까지 나머지가 0이 나오는 숫자가 약수
    for su in range(2, idx// 2 + 1):
        if idx % su == 0:
            hap = hap + su

    #완전수 판별
    if idx == hap:
        cnt = cnt + 1
print(cnt)



#문제2
#피보나치 수열
#첫번째와 두번째 데이터는
#세번째 데이터부턴느 앞의 2개의 합
#1, 1, 2, 3, 5
#n번째 피보나치 수열의 값을구하는 로직을 작석


#def ffi(n):
#   if n <= 1:
#        return n
#    else :
#        return(ffi(n-1) + ffi(n-2))

#for i in range(1,10):
#    print(ffi(i))

#몇번째 피보나치 수열의 값을 구할지 입력
n = int(input("구하고자 하는 피보나치 수열의 값은?"))

if n == 1 or n == 2:
    print(1)

else:
    n_1 = 1 #직전 항
    n_2 = 1 #두번째 앞의 항
    result = 0 #실제 결과
    for i in range(3, n+1):
        result = n_1 + n_2
        n_2 = n_2
        n_1 = result
    print(result)
