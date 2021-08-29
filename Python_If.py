# 조건문  if

# 조건문 문법

# if 조건:
# 실행 명령문
print("-----------------")
print("여러줄 들여쓰기 테스트1")
weather = "비"
if weather == "비": # = 은 2번 써야한다.
    print("weather : ",weather)
    print("우산을 챙기세요.")
    print("여기도 되려나?")
#들여쓰기를 안하는 순간 조건문 영역에서 벗어난다.
print("-----------------")
# 조건문의 if 위치를 기준으로 공백(스페이스) 4칸씩 들여쓰기를 해야한다.

print("여러줄 들여쓰기 테스트2")
weather = "맑음"
if weather == "비":
    print("weather : ",weather)
    print("우산을 챙기세요.")
print("-----------------")

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지": #elif 는 else if 
    print("마스크를 챙기세요.")

weather = "맑아요"

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없다.") #else는 모두에 해당안할 때

# input()을 사용하면 사용자로부터 입력값을 받는 용도
# 입력값은 문자열값으로 받아진다. ""붙어서

#입력 값을 다르게 테스트
print("-------입력값변경테스트-------")

print(weather) # 사용자가 입력한 값 출력
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없다.") 

print("---------여러조건 검색 or처리------------")
weather = input("오늘 날씨 어때요?")
print(weather) # 사용자가 입력한 값 출력
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없다.") 

print("--------입력값의 형변환------------")
temp = int(input("온도가 몇도인가요?"))
if temp >= 30:
    print("더우니 반팔입자.")
elif temp < 30 and temp >= 15:
    print("선선해요.")
elif temp < 15 and temp >= 5:
    print("추우려나")
else:
    print("춥다.")