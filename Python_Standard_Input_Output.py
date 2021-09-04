# 표준입출력

print("1. 표준 출력에 대하여")

# 지금까지 공부하였던 print()문의 문법을 살펴보자

print("Python", "Java")  # Python Java
print("Python" + "Java") # PythonJava

# 지금까지는 문자열를 구분지을 경우 ,를 사용하게되면 문자열사이에 ", "와 같은 형태로 구분지어져 있었다. 
# 그렇기에 불편하더라도 print()문을 사용할 때 + 를 사용하며 코딩하였었다.

print("-----sep옵션-----")
# 문자열을 구분짓는 방법을 직접 정의 할 수 있다.
# sep(separator)옵션을 사용하면 된다.

print("Python", "Java", sep=",") # Python,Java # 값들을 콤마(,)로 구분

print("Python","Java","JavaScript", sep=" vs ") # Python vs Java vs JavaScript

print("-----end옵션-----")
# print()문은 기본적으로 문장이 끝날때마다 줄바꿈을 하기 때문에 연속적으로 2개 이상의 print()을 이용하면 각각의 줄에 내용이 출력된다.
# 이것을 방지해주는 옵션이 end옵션

print("Python", "Java", sep= ",", end="?") # Python,Java?무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

# end에 값을 입력하지 않을경우.
print("Python", "Java", sep= ",", end="") # Python,Java무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

print("-----sys모듈-----")
import sys # sys모듈을 가져와서 사용하겠다는 의미
print("Python", "Java",file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# 현 시점 파이썬 기본편을 공부하는 시점에서는 이부분에 대하여는 이런게 있다정도로만 인지하고 있으면 된다고 한다.
# 다만 여기서 덧붙여 기술하면 로그 출력시 이와같이 구분지어 둘 경우 에러가 발생시 에러 로그만 확인할수 있는 장점이 있기에 편할 수 있다.

print("-----ljust(), rjust() 적용전-----")
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items(): #key, value
    print(subject, score)

# 수학 0
# 영어 50
# 코딩 100
print("-----ljust(), rjust() 적용후-----")
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items(): #key, value
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
# rjust(), ljust()함수는 기본적으로 문자열 편집함수이다. 그렇기에 형변환이 필수

# 수학      :   0
# 영어      :  50
# 코딩      : 100


# rjust(x),ljust(x)함수의 동작원리
# 1. 함수의 파라미터 x의 갯수만큼 공간을 확보
# 2. r인지 l인지에 따라 기준에 맞게 값을 채우기
# 3. sep와 같은 옵션은 나중에 처리.
# 값이 채워지지 않은 공간은 비어있는 상태로 표가

print("-----zfill() 적용전-----")
# 번호표를 뽑았을 때 숫자의 앞자리가 0이 붙어있는 채 출력되도록 한다.
for num in range(1,21): #1 ~ 20까지의 숫자
     print("대기번호 : "+ str(num))

# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# ... 생략 ...
# 대기번호 : 18
# 대기번호 : 19
# 대기번호 : 20

# 자릿수가 달라지면서 출력 형태가 달라진다.
# 이를 해결하는 방법은 빈공간을 0으로 채워주는 zfill
print("-----zfill() 적용후-----")
for num in range(1,21): #1 ~ 20까지의 숫자
     print("대기번호 : "+ str(num).zfill(3))

# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# ... 생략 ...
# 대기번호 : 018
# 대기번호 : 019
# 대기번호 : 020

print("2. 표준 입력에 대하여")

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값의 타입은 : " + str(type(answer)))# 입력하신 값의 타입은 : <class 'str'>
print("입력하신 값은 " + answer + "입니다.")

# 입력받은 값을 숫자로써 계산 목적으로 사용하려면 반드시 int(answer)와 같이 형변환이 필요하다.


# 입력받은 값을 곧바로 숫자형으로 이용하고 싶을 경우는 다음과 같이 활용가능하다.
answer2 = int(input("아무 값이나 입력 : "))
print("입력한 값에 10을 더하면 "+ str(answer2+10))
