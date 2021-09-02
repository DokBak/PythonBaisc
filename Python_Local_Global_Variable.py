# 지역변수, 전역변수

print("-----전역변수 에러가 발생하는 코드-----")
# gun = 10 # 총 10 자루
# def checkpoint(soldiers): # 경계근무 나가는 군인의 수 
#     gun = gun - soldiers # 전체 총에서 경계근무 나가는 군인 수만큼 뺀 잔여 총
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun)) # 10자루
# checkpoint(2) # 2명이 경계 근무 출발
# print("남은 총 : {0}".format(gun)) # 몇자루?

# 위 코드가 에러가 발생하는 원인은 코드 작성 순서때문에 헤깔리는 내용이다.
# 함수 checkpoint의 파라미터로 gun이 들어온것도 아닌데 선언도 안된 gun을 사용하려고 하니 에러가 발생한다.

print("-----함수 내에 변수를 선언-----")
# gun = 10 
# def checkpoint(soldiers):
#     gun = 20 # 변수 선언 추가
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun)) 
# checkpoint(2) 
# print("남은 총 : {0}".format(gun)) 

# 전체 총 : 10
# [함수 내]남은 총 : 18
# 남은 총 : 10

print("-----전역 변수를 수정-----")
# gun = 10 # 총 10 자루
# def checkpoint(soldiers): 
#     global gun # 전역공간에 있는 gun이라는 변수를 사용
#     gun = gun - soldiers 
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun)) 
# checkpoint(2) 
# print("남은 총 : {0}".format(gun)) 

# 전체 총 : 10
# [함수 내]남은 총 : 8
# 남은 총 : 8

print("-----전역 변수를 활용하는법, 전달값으로 사용하기-----")
gun = 10 # 총 10 자루
def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun)) 
checkpoint_ret(gun,2) 
print("남은 총 : {0}".format(gun)) 

# 전체 총 : 10
# [함수 내]남은 총 : 8
# 남은 총 : 8