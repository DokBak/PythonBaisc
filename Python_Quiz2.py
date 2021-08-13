#퀴즈2

# 월 4회중 3회는 a에서 1회는 b에서
# 날짜는 랜덤함수로 뽑아야한다.
# 한 달을 28일로 계산한다.
# 매 월 1~3일은 제외한다.

from random import * 

#b에서의 1회
a = randint(4,28)
print("a = randint(4,28)")
print("b에서의 1회는",a,"일로 선정")


#해설
date = randint(4,28)
print("date = randint(4,28)")
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + +"일로 선정되었습니다.")
