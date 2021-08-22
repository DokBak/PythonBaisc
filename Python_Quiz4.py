#퀴즈4

# 당신은 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복은 불가
# 조건3 : random모듈의 shuffle과 sample을 활용 

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

print("random모듈의 shuffle, sample연습")
print("-----------------------------")

from random import *
lst = [1,2,3,4,5]
print(lst) # 원본 리스트
shuffle(lst) # 리스트를 뒤섞기
print(lst) # 섞은 후 리스트
print(sample(lst,1)) # 리스트 내에서 1개를 무작위로 뽑기
print("-----------------------------")

print("본 문제")
event = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(event)
pickevent = sample(event,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ",pickevent[0],"\n커피 당첨자",pickevent[1:4])
print("-- 축하합니다 --")

print("-----------------------------")

print("예시 정답")

users = list(range(1,21))
print(users)
shuffle(users)
print(users)
chicken_winner = sample(users,1)

remain_user = set(users) - set(chicken_winner)
coffee_winner = sample(remain_user,3)

print(chicken_winner)
print(coffee_winner)

print("치킨 당첨자 : {0}" .format(chicken_winner))