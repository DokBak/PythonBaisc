#파이썬 숫자 처리 함수 
#abs(x)=|x| 절대값
print("abs(4) : ",abs(4)) #4
print("abs(-4) : ",abs(-4)) #4

#pow(a,b)=a^b 제곱
print("pow(4,3) : ",pow(4,3)) #4^3

#max(a,b)=b (a<b) 최대값
#파라미터는 2개 이상도 가능하다.
print("max(8,9,11,40) : ",max(8,9,11,40)) #40

#min(a,b)=a (a>b) 최소값
#파라미터는 2개 이상도 가능하다.
print("min(6,9,23,40) : ",min(6,9,23,40)) #6

#round(a) (a는 실수) 정수화(반올림)
print("round(3.14) : ",round(3.14)) #3
print("round(4.78) : ",round(4.78)) #5

print("round(4/2)  ",round(4/2)) #2
#나눗셈을 하게되면 정수형이 아닌 실수형으로 결과값이 나와서 나누어 떨어지더라도 .0의 값이 나오는데 정수화 시키는 방법이다.

#파이썬에서는 사용하고 싶은 모듈을 다음과 같이 사용 가능하다.
# C#에서 using 선언하듯 from 모듈명 import 함수명
from math import * # math 모듈을 모두 사용하겠다는 의미

print("math모듈을 모두 사용하겠다는 선언으로 다음과 같이 작성한다.")
print("from math import *")
#floor(4.76)=4 4.76의 내림
print("floor(4.78) : ",floor(4.78)) #4

#ceil(3.22)=4 3.22의 올림
print("ceil(3.22) : ",ceil(3.22)) #4

#sqrt(16)=4 제곱근
print("sqrt(16) : ",sqrt(16))
#나눗셈을 하면 소수점이 나오는것과 같이 sqrt() 또한 정수로 나눠지더라도 실수의 형태로 출력된다.

#모듈을 사용할때 선언문을 26줄과 같이 from math import *로 사용해도 되지만
#import math로도 선언가능하다.

import math
print("import math")
print("로 출력될 경우는 함수를 사용할때 모듈명도 같이 작성해주어야한다.")

print("math.floor(4.78) : ",math.floor(4.78))
print("math.ceil(3.22) : ",math.ceil(3.22))
print("math.sqrt(16) : ",math.sqrt(16))


# 2021년 9월 4일 추가 내용 
# 기존의 round함수는 단순 실수를 정수형으로 변경시 반올림이 된다 정도로만 공부하였는데 파라미터를 하나 더 추가함으로써 원하는 자릿수에서 반올림이 가능하다.

testData = 12345.746
print(round(testData))   # 12346 
print(round(testData,1)) # 12345.7
print(round(testData,2)) # 12345.75
print(round(testData,3)) # 12345.746
print(round(testData,-1))# 12350.0 역으로 반올림으 실행한 경우에는 .0 이 남아 실수형으로 출력된다.
print(round(testData,-2))# 12300.0 역으로 반올림으 실행한 경우에는 .0 이 남아 실수형으로 출력된다.
