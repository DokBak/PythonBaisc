# 키워드 인자

# 지금까지의 함수는 아래와 같이 사용했었다.
print("-----기본값 함수 구조-----")
def profileFunction(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profileFunction("유재석",20,"파이썬") # 유재석씨(20세)의 주 사용 언어는 파이썬
profileFunction("김태호",25,"자바")  # 김태호씨(25세)의 주 사용 언어는 자바

# 순서에 구애받지 않으면서, 기본값을 쓰고 필요한 부분만 콕 찍어서 값을 전달하고자 하는 경우 사용한다.
print("-----키워드 함수 구조-----")
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name = "유재석", main_lang="파이썬", age = 20) # 유재석씨(20세)의 주 사용 언어는 파이썬
profile(main_lang = "자바", age = 25, name = "김태호")  # 김태호씨(25세)의 주 사용 언어는 자바
