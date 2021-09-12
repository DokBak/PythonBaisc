# Python_Module.py에서 모듈 사용법을 공부하기 위해 만든 파이썬 파일

# 사람 수에 따른 영화표 가격을 계산해주는 3개 함수를 정의 

# 일반 가격 
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_moring(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 10000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 10000))

    