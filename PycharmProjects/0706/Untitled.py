#!/usr/bin/env python
# coding: utf-8

# In[4]:


#동일한 블럭에서는 들여쓰기를 맞추어야하지만 다른 블럭의 경우는 맞출 필요 없음
num = 20
if num >= 10:
    print("10보다 크거나 같다 ")
else :
    print("10보다 작다")


# In[16]:


#주석

"""

이 문장은 문자열 상수를 만드는 문장인데 대입도 하지 않았고

출력에 이용하지도 않았기 때문에 주석처럼 처리됨.

"""
data = "Hello Python"
print(dir(data))

help(sum)

print(sum([1,2,3]))
print(sum({1,2,3}))
print(sum((1,2,3)))


# In[14]:


import keyword

print(keyword .kwlist)


# In[9]:


import sys

print(sys.path)


# In[10]:


a = 10
b = 10
print(id(a))
print(id(b))


# In[11]:


print(dir(set))


# In[18]:


condition =20
if condition > 5;
    data = 20
else : 
    data = 5
    print(data)


# In[22]:


print([1, 2, 3]+[4, 5]) #데이터의 모임의 경우는결합
#print("문자열"+3)  #문자열과 숫자는 종류가 달라서 에러
print((1, 2, 3) * 3) #데이터 모임 *정수 = 반복
print("Hello\3"*5) # \n으로 줄바꿈 가능함


# In[24]:


print(20 & 17)
print(20 | 17)
print(20 ^ 17)
print(~ 20)
print(20 << 3)
print(20 >> 3)


# In[25]:


cnt = 0 #12의 배수의 개수를 저장하기 위한 변수
loop = 0 #조건 확인한 개수를 저장하기 위한 변수
for idx in range(1, 101):
    loop =loop +1
    if idx % 3 == 0:
        loop = loop + 1
        if idx % 4 == 0 :
            cnt = cnt + 1
print("12의 배수의 개수:", cnt) #12의 배수의 개수를 저장하기 위한 변수
print("조건 확인 개수:", loop ) #조건 확인한 개수를 저장하기 위한 변수


# In[27]:


year = 2023  #년도
#윤연의 조건 - 둘 중 하나만 True이면 True -> or
#1. 4의 배수이고 100의 배수가 아닌 경우
#2. 400의 배수인 경우
#(1, 2 중 확률이 높은 것을 앞에 두어야함)
if year%4 == 0 and year % 100 != 0  or year % 400 == 0:
    print(year,"는 윤년")
else:
    print(year,"는 유년이 아님")


# In[28]:


help(print)


# In[29]:


help(input)


# In[30]:


name = input("이름 입력 :")
print(name)


# In[31]:


try:
    age = int(input("나이입력:"))
    print(age + 1 )

except :
    print("프로그램 종료")
    
## 문자열을 정수로 변환
age = int(input("나이입력:"))
print(age + 1 )

#여러개 입력
hobbys = input("취미를 , 로 구분해서 입력").split(",")
for hobby in hobbys:
    print(hobby)


# In[ ]:




