#문자열 처리 함수 공부

python = "Python is Amazing"

#문자열을 소문자로 변환
print(python + "을(를) 문자열 함수 lower() 사용하면 : " + python.lower())
#문자열을 대문자로 변환
print(python + "을(를) 문자열 함수 upper() 사용하면 : " + python.upper())


#islower,isupper를 사용할떄는 변수의 n번째 인덱스를 확인하는 함수이다. 
#문자열의 n번째 인덱스가 소문자인지 확인
print(python + "을(를) 문자열 함수 islower() 사용하면 : " + str(python[0].islower()))
#문자열의 n번째 인덱스가 대문자인지 확인
print(python + "을(를) 문자열 함수 isupper() 사용하면 : " + str(python[0].isupper()))

#문자열의 길이를 체크(띄어쓰기 포함)
print(python + "을(를) 문자열 함수 len() 사용하면 : " + str(len(python)))

#문자열 내의 특정 문자열을 원하는 문자열로 치환
print(python + "을(를) 문자열 함수 replace() 사용하면 : " + python.replace("Python","Java"))

#문자열 내에 어떤 문자가 어느 위치에 있는지를 확인하는 함수
#index()와 find()의 차이는 검색할 문자열이 없을때 차이가 있다.
#index() : 검색문자열이 없을 경우 에러가 발생하며 프로그램 종료
#find() : 검색문자열이 없을 경우 -1을 반환하며 프로그램 수행
print(python + "을(를) 문자열 함수 index() 사용하면 : " + str(python.index("n")))
print(python + "을(를) 문자열 함수 find() 사용하면 : " + str(python.find("n")))

#찾으려는 문자열이 총 몇 번 사용되었는지 확인 
print(python + "을(를) 문자열 함수 count() 사용하면 : " + str(python.count("n")))
