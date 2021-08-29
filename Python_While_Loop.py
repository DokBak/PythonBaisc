# 반복문 While

# for뿐만아니라 반복문에는 while도 있다.

# 문법
# while 조건:
#   실행명령문1
#   실행명령문2

user = "A" # 손님
index = 5 # 부르는 횟수 5회

while index >= 1: #부르는 횟수가 1이상인 경우에만 반복 실행
    print("{0}, 커피가 준비 되었습니다.{1}번 남았습니다.".format(user,index))
    index -=1 # 부르는 횟수 감소
    if index == 0:
        print("커피는 폐기처분되었습니다.")

user = "B"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회." .format(user,index))
    index += 1
    if index == 5: # 예제종료를 위한 직접 추가
        break      # 예제종료를 위한 직접 추가
# 프로그램을 강제 종료 시킬 경우의 단축키
# control + c   맥북기준으로 control이다 command가 아님

user = "C"
person = "Unknown"

while person != user:
    print("{0}, 커피가 준비 되었습니다.".format(user))
    person = input("이름이 어떻게 되세요?")