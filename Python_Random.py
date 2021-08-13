#랜덤함수 공부
from random import * #random 모듈에서 모든 것을 가져다 쓰겠다는 의미

print("random() : ", random()) #random()함수의 기본 값 :0.0 이상 1.0 미만의 임의의 값 생성

print("random() * 10 : ", random() * 10) #0.0 이상 10.0미만의 임의의 값 생성
print("int(random()) * 10 : ",  int(random() * 10)) # 0이상 10미만의 임의의 정수 값 생성
print("int(random() * 10) + 1 : ", int(random() * 10) + 1) # 1 이상 10이하(11미만)의 임의의 정수 값 생성

#int()함수는 
#로또 번호생성하고자 한다면?

print("int(random() * 45 + 1) : ",int(random() * 45 + 1)) #정답 1   (0 <= X < 45)+1 
print("int(random() * 45) + 1 : ",int(random() * 45) + 1) #정답 2   (0 + 1 <= X ＜ 45 + 1)

#가급적이면 (랜덤함수 * 최대숫자) + 1 과 같은 형식으로 작성하는 것이 범위를 파악하기 쉬워보인다.

#하지만 파이썬에서는 보다 쉽게 원하는 범위 내의 랜덤 수를 뽑는 함수들을 제공함

#randrange(a,b) : 주어진 범위 내의 임의의 정수 값 생성 (a이상 b미만의 임의의 정수)
print("randrange(1,46) : ",randrange(1,46)) # 1이상 46미만의 임의의 정수 값 생성

#randint(a,b) : 주어진 범위 내의 임의의 정수 값 생성 (a이상 b이하)
print("randint(1,45) : ",randint(1,45)) # 1이상 45이하의 임의의 정수 값 생성
