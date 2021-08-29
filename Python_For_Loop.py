# 반복문 for

# 문법
# for 변수 in 반복대상
#   실행명령문1
#   실행명령문2
print("---------리스트를 직접 입력------------")
for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no)) #{0}위치에는 waiting_no 

from random import *
print("---------랜덤함수를 입력------------")
for waiting_no in range(1,6): #0부터 5직전까지 (0~4)
    print("대기번호 : {0}".format(waiting_no))

print("---------리스트를 입력------------")
starbucks = ["A","B","C"]
for user in starbucks:
    print("{0}, 커피가 준비되었다.".format(user))