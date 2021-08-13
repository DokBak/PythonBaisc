# PythonBaisc
PythonBaisc

작업내용

2021년 8월 13일
    랜덤 함수(Python_Random.py)
        랜덤함수를 사용할 때는 (from random import * )로 랜덤모듈을 선언한다.
        random() : 0 <= X < 1 (0이상 1미만)
        randrange(a, b) : a <= X < b (a이상 b미만)
        randint(a,b) : a <= X <= b (a이상 b이하)
    간단 퀴즈(Python_Quiz2.py)
        랜덤함수에 사용에 대해 생각해 볼 수 있는 문제
    문자열 공부(Python_String.py)
        문자열 선언시 큰 따옴표("), 작은 따옴표(') 어느 것을 사용해도 상관없다. 여러줄 문자열 선언은 같은 따옴표로 3개를 사용하면 된다.
        변수 뒤에 붙는 경우는 다중 주석으로 인식하지 않는다.
    슬라이싱 공부(Python_Slicing.py)
        문자열을 선택해서 원하는 문자열만 추출하는 방법
        문자열[0:3], 문자열[:4], 문자열[4:7], 문자열[:] ,문자열[-7]
    문자열 처리 함수(Python_String_Function.py)
        문자열.lower()
        문자열.upper()
        문자열[n].islower()
        문자열[n].isupper()
        문자열.replace("변경하려는 문자열","변경된 문자열")
        문자열.index("n")
        문자열.find("n")
        문자열.count("n")
2021년 8월 10일 
    변수 공부(Python_Parameter.py)
        변수를 출력할 때, 문자형 변수는 그대로 출력가능하다.
        문자형과 다른 숫자형, 불리언형은 형변환을 실시후 출력하여야 에러가 나지 않는다.-> 형변환 : str()
        출력을 할때 "문자열 + 변수 + 문자열"로 출력하는 것 이외
        쉼표(,)를 사용해 출력가능하다.
            쉼표로 출력시에는 쉼표부분이 공백으로 출력된다.이 때는 형변환을 실시하지 않아도 에러가 나지 않고 출력가능하다.
    주석 공부(Python_Comment.py)
        주석이란 코딩을 할 경우 그에 대한 부연설명을 코드에 영향을 주지 않고 설명을 하는 목적용으로 사용하기 위해서 작성하는 내용으로
        강제는 아니지만 적어주는것이 좋다.
    간단퀴즈(Python_Quiz1.py)
        변수의 사용방법에 대하여 생각해보는 간단한 퀴즈
    연산자 공부(Python_Operator.py)
        기본연산자(덧셈(+),뺄셈(-),곱셈(*),나눗셈(/))
        특수연산자(제곱(**),나머지연산(%),몫연산(//))
        비교연산자(>,>=,<,<=)
        논리연산자(and, or, not)
            a > b > c 연산에서 a > b가 먼저 거짓으로 판명나게되면 후속 조건인 b > c는 연산하지 않는다.
    간단수식 공부(Python_Equation.py)
        간단한 a와 b 두 개의 항만으로 계산을 할 경우
        (+=,-=,*=,/=,**=,%=,//=)
    숫자처리함수 공부(Python_Math_Equation.py)
        숫자처리함수(math)에 대한 공부
        선언방법
        1. from math import *
        2. import math

        1의 경우에는 해당 함수만으로 사용가능한데(예시 : sqrt(16)), 2의 경우는 함수명 앞에 모듈명까지 작성(예시 : math.sqrt(16))해 주어야한다. 

        abs(a),pow(a,b),max(a,b,c,d),min(a,b,c,d),round(a),floor(a),ceil(a),sqrt(a)

2021년 8월 9일 디버그 설정
    디버그를 사용하기위해 launch.json파일을 생성하였다.
    데이터 타입 공부(Python_Parameter.py)

2021년 8월 7일 프로젝트 생성
    깃허브와의 연동
        vs code에서 f1키를 누르고 Git:clone을 입력해서 깃허브에 만들어두었던 레포지토리와 연동시켜준다.
        vs code에서 작성한 소스를 깃허브에 올릴 때는 소스제어 메뉴에서 체크버튼(커밋)을 실행한뒤에 ...에서 푸시를 해주어야 올라간다.

  
