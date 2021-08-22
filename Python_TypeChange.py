# 자료구조의 변경

#세트변수로 선언
menu = {"커피", "우유", "주스"}
print(menu,type(menu)) #{'주스', '우유', '커피'} <class 'set'>

menu =  list(menu)
print(menu,type(menu)) #{'주스', '우유', '커피'} <class 'list'>

menu = tuple(menu)
print(menu,type(menu)) #{'주스', '우유', '커피'} <class 'tuple'>

menu = set(menu)
print(menu,type(menu)) #{'주스', '우유', '커피'} <class 'set'>

# 각각의 형태는 다들 비슷하나 각각의 구조의 특징을 잘 습득해두자.

stri = "변수테스트"
inti = 123
print(type(stri)) #<class 'str'>
print(type(inti)) #<class 'int'>
