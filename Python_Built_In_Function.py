# 내장 함수

# 내장 함수란 별도로 import를 하지 않고도 사용할 수 있도록 내장되어 있는 함수를 의미한다.

# 내장 함수 : input() 값을 입력받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# 내장 함수 : dir() 어떤 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 목적으로 사용, 
#           전달값을 아무것도 넘기지 않는다면 현재 소스코드 범위 내에서 사용 가능한 모듈 또는 객체가 출력된다.

print("--사용가능한 모듈 또는 객체 출력--")
print(dir()) # 기본 값들만 출력
import random # random 모듈 가져다 쓰기
print(dir()) # random을 추가해서 출력
import pickle # pickle 모듈 가져다 쓰기
print(dir()) # pickle을 추가해서 출력

print("--random모듈 내에서 사용가능한 모든것을 출력--")
print(dir(random))

print("--모듈이 아닌 리스트 자료구조를 만들어 확인")
lst = [1,2,3]
print(dir(lst))

print("--문자열 변수를 확인")
name = "Jim"
print(dir(name))

# 파이썬에서 제공되는 내장 함수에 대한 더 자세한 내용은 구글에 list of python builtins로 검색하면 나오는 파이썬 공식 홈페이지에서 확인 가능하다.
# 사이트 : https://docs.python.org/3/library/functions.html