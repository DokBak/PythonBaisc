# 퀴즈6

# 표준체중을 구하는 프로그램을 작성하시오.
# * 표준 체중 : 각 개인의 키에 적당한 체중 

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산 
#   * 함수명 : std_weight
#   * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

#(출력 예제)
# 키 175cm남자의 표준 체중은 67.38kg입니다.

def std_weight(height,gender):
    if((gender == "남자") or (gender == "man") or (gender == 1)):
        weight = (height * 0.01) * (height * 0.01) * 22
    elif((gender == "여자") or (gender == "woman") or (gender == 2)):
        weight = (height * 0.01)  * (height * 0.01) * 21
    weight = round(weight,2) # 반올림으로 표기
    return weight

height = 175 #cm
gender = "여자"
weight = std_weight(height,gender)
print("-----출력방식1-----")
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg입니다.")
print("-----출력방식2-----")
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))
print("-----출력방식3-----")
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,std_weight(height,gender)))
print("-----출력방식4-----")
print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height,gender,weight))
print("-----출력방식5-----")
print("키 {height}cm {gender}의 표준 체중은 {weight}kg입니다.".format(height = 190,gender = "남자", weight=std_weight(height=190, gender="남자")))

# 블로그에있던 다른분 표기방법
# 콘솔에 값을 입력받아 표준체중을 계산 : 이 경우에 입력받은값은 문자열로써 받아들여지기 때문에 반드시 형변환을 해줘야한다. 
height = int(input("자신의 키를 입력해주세요."))
gender = input("성별을 입력해주세요. 예)남자")
wieght = std_weight(height,gender)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg입니다.")