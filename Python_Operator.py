#연산자 공부

#연산자란 쉽게 말해 더하기(+), 빼기(-), 곱하기(*), 나누기(/)를 의미한다.

print("----기본 연산자")
#덧셈 연산(+)
print("1+1 : ",1+1) #2
#뺄셈 연산(-)
print("2-1 : ",2-1) #1
#곱셈 연산(*)
print("3*4 : ",3*4) #12
#나눗셈 연산(/)
print("6/2 : ",6/2) #3.0
#나눗셈의 경우에는 연산 결과 값이 정수가 아닌 필요시,자동으로 실수형으로 변환되어 표현된다.

print("----특수 연산자")
#제곱 연산(**)
print("4**2 : ",4**2) #16
#나머지 연산(%)
print("5%3 : ",5%3) #2
#몫 연산
print("7//2 : ",7//2) #3

#비교 연산
print("----비교 연산자") #비교연산의 결과는 True와 False로 출력
# ~보다 크다
print("9>8 : ",9>8) #True
# ~보다 크거나 같다
print("8>=9 : ",8>=9) #False
# ~보다 작다
print("3<8 : ",3<8) #True
# ~보다 작거나 같다
print("3<=9 : ",3<=9) #True
# 좌항, 우항이 같다.
print("10==11 : ",10==11) #False
# 좌항, 우항이 다르다.
print("10!=11 : ",10!=11) #True

print("----논리 연산자")
#and연산자
print("(3>=1)and(3>8) : ",(3>=1)and(3>8))#False
#or연산자
print("(3>=1)or(3>8) : ",(3>=1)or(3>8))#True
#not연산자
print("not(5>2) : ",not(5>2))#False

print("----파이썬특수 논리연산")
# 좌측부터 연산한다. 
# (5>4)도 (4>3) 참이므로 참이 출력된다.
print("5>4>3 : ",5>4>3) #True
# (5>4)은 참이나 (4>7)가 거짓이라 거짓이 출력된다. 
print("5>4>7 : ",5>4>7) #False
# a > b > c 연산에서 a > b가 먼저 거짓으로 판명나게되면 후속 조건인 b > c는 연산하지 않는다.
