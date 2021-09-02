# 기본값 설정

# 구조체 겸 함수의 짬뽕정도로 생각하면 좋은듯 싶다.
# 기본 구조형, 초기값 설정을 굳이 안해도 된다.
print("-----기본값 구조-----")
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석",20,"파이썬") # 유재석씨(20세)의 주 사용 언어는 파이썬
profile("김태호",25,"자바")  # 김태호씨(25세)의 주 사용 언어는 자바

# 기본값을 미리 설정해두면 설정값은 파라미터를 입력하지 않아도 된다.
print("-----기본값 설정방법-----")
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

# 기본값 설정 예시
profile("노홍철")          # 이름 : 노홍철   나이 : 17       주 사용 언어 : 파이썬
profile("노홍철",30)       # 이름 : 노홍철   나이 : 30       주 사용 언어 : 파이썬
profile("노홍철",30,"루비") # 이름 : 노홍철   나이 : 30       주 사용 언어 : 루비