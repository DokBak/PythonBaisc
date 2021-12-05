# **Python PythonBaisc**

## **Development Environment**
### 1. OS : MacOS Big Sur 11.5.2
### 2. Language : Python 3.9.7
### 3. IDE : VS CODE

## Study reference : youtube="nadocoding", blog=nadocoding.tistory.com

## Work
2021년 10월 4일
    파이썬 exe파일 생성
        1. pyinstaller 설치
            - pip install pyinstaller
        2. pyinstaller ‘.\파일명.py’
            - ‘’은 생략해도 되나 공백이 있는 경우에는 따옴표가 필수
            - 옵션 없이 작성시에는 exe 파일을 실행시키기위한 모든 파일들도 생성되게 된다.
        3. pyinstaller -F ‘.\파일명.py’
            - 옵션을 -F을 작성하면 exe파일하나로 압축 생성되어진다.
        4. pyinstaller -w ‘.\파일명.py’
            - 옵션을 -w을 작성하면 윈도우 프로그램으로 인식하여 GUI 프로그램으로 인식한다.
            - 이때 다른 폴더에 포함된 파일을 참조하는 코드가 있는경우 해당 폴더와 파일을 동일한 경로에 넣어주어야 프로그램이 정상작동한다.
        5. pyinstaller -w -F ‘.\파일명.py’
            - 압축된 exe파일을 풀 때의 경로가 매번 바뀌기에 그 문제를 해결하는 내용을 추가 해주어야한다.
            - 구글에 [pyinstaller add folder with images in exe file] 검색해서 나온 결과는 아래와 같다.
        		import os
	        	def resource_path(relative_path):
		            try:
		                base_path = sys._MEIPASS
		            except Exception:
		                base_path = os.path.abspath(".")
		            return os.path.join(base_path, relative_path)

            - 위의 코드를 외부 파일을 참조할때 참조 파일등의 경로를 위의 함수를 사용하면 상대경로가 절대경로로 변경되어 적용된다.
        6. pyinstaller -w —add-data ‘src:dest’ ‘.\파일명.py’
            - ’src:dest’ 에서 src는 추가할 파일, :는 맥의 경우(;은 윈도우의 경우), dest는 어느 위치에 넣을지 같은경로라면 .으로 입력
        7. pyinstaller -w —add-data ‘src:dest’  -F ‘.\파일명.py’
            - 최종적으로 exe파일 하나로 생성되도록하는 프로그램 하는 작업

2021년 9월 13일 
    파이썬패키지검색(Python_Package_Search.py)
        1. 파이선의 패키지를 검색해서 다운로드를 하기 위해선 pip를 사전에 설치를 해주어야 한다.(공식 파이썬 사이트에서 파이썬을 설치할 경우pip를 찾지 못하는 경우가 있다.)
        2. 패키지 검색 사이트(https://pypi.org)에서 원하는 패키지를 검색해서 사용가능하다.
        3. 다운로드 시에는 터미널에 해당 패키지 내용을 입력해 다운로드한다. pip install [패키지]
    내장함수(Python_Built_In_Function.py)
        1. 별도의 import를 하지 않고도 사용할 수 있도록 내장되어 있는 함수를 말한다.
        2. dir() : 전달값을 입력하지 않고 사용하면 현재 소스코드 범위 내에서 사용가능한 모듈 또는 객체가 출력된다.
                   전달값으로 어떤 객체, 모듈을 넘기면 그 객체가 어떤 변수와 함수를 가지고 있는지 알려준다.
        3. 구글에 list of python builtins로 검색하면 나오는 파이썬 공식 홈페이지에서 자세한 내용을 확인가능하다.
            사이트 : https://docs.python.org/3/library/functions.html
    외장함수(Python_Built_Out_Function.py)
        1. 내장 함수와 달리 import를 해야 사용가능한 모듈을 말한다.
        2. glob
            glob() : 작업공간내의 파일을 검색
        3. os
            getcwd() : 현재 디렉토리
            path.exists() : 전달값 폴더명이 존재하는지 판단
            makedirs() : 전달값 이름의 폴더를 생성
            rmdir() : 전달값 이름의 폴더를 삭제
            listdir() : 현재 작업 디렉토리 내의 폴더와 파일 목록을 출력
        4. time
            localtime() : 현지의 시간을 출력(알아보기 힘들다...)
            strftime() : 지정된 형식으로 시간이 출력된다.
                %Y : 연
                %m : 월
                %d : 일
                %H : 시
                %M : 분
                %S : 초
        5. datetime
            date.today() : 오늘의 날짜(연도-월-일)형식으로 출력된다.
            timedelta() : 지정된 날짜만큼 계산할 날짜를 저장한다.
    퀴즈10(Python_Quiz10.py)
        byme.py 파일을 만들어 사용할 Python_Quiz10.py에서 import 후 함수를 실행.
        
2021년 9월 12일
    모듈(Python_Module.py)
        1. 모듈이란  C#에서 dll과 같은 것.
        2. 기존 모듈 포함시키는 방법
            a. import ~
                모듈명.함수 의 형식으로 사용한다
            b. from ~ from * 
                함수 의 형식으로 사용한다. (모듈명 생략가능)
        3. 사용자 정의 모듈용 파일은 사용하고자 하는 파일과 동일한 경로에 있어야 사용가능하다.(기본 라이브러리 폴더에 있어도 가능한가 보다.)
        4. 별명 설정(모듈명이나 함수명이 길 경우 재설정하여 사용한다.)
            a. import ~ as 별명
                별명.함수 의 형식으로 사용가능하게 만들어준다.
            b. from ~ from 함수명 as 별명
                별명 의 형식으로 사용한다. 기존의 함수명을 별명으로 바꿔 사용 가능하다.
        ?. 모듈_예제(theater_module.py)
            모듈(Python_Module.py)에서 연습용으로 만든 파일.
        ?. 사용자 정의 모듈을 사용한 경우에는 __pycache__폴더 및 사용자 정의 파일관련 .pyc파일이 생성된다.         
    패키지(Python_Package.py)
        1. 여러 모듈들을 모아 놓은 집합을 패키지라한다. 
        2. 클래스나 함수를 import할 수 없다. import는 모듈이나 패키지만 가능하다.
    모든 메서드 참조(Python_All.py)
        1. 패키지에 참조가능한 모듈을 설정가능하다.
        2. 패키지에 __init__.py 파일을 만들고 __all__ 변수를 만들어 [사용할 모듈명]을 입력 
    모듈 직접 실행(Python_Module_Execute.py)
        1. 패키지의 모듈을 사용할 떄 패키지 모듈에 작성할 내용 
            if __name__ == "__main__": # 직접 실행되는 경우
                pass
            else: # 외부에서 호출되어 실행되는 경우
                pass 
        2. 모듈을 직접 실행할 경우와 호출되어 실행할 경우를 나누어 작성 가능하다.
    패키지, 모듈위치(Python_Package_Module_Location.py)
        1. 사용하고자하는 패키지나 모듈은 호출하려는 파일과 동일한 경로에 있거나 파이썬라이브러리 폴더에 있어야한다.
        2. import inspect로 모듈이 저장된 위치를 확인가능하다.
            inspect.getfile(모듈명)
        3. 사용자 정의 패키지 파일을 기본 파이썬 라이브러리 폴더에 넣으면 random함수 처럼 모든 파이썬프로젝트에서 사용가능하다.

2021년 9월 11일
    퀴즈8(Python_Quiz8.py)
        1. 클래스로 인스턴스를 만들어 한번에 관리 하고자 할때는 배열에 넣어서 일괄처리한다. 
        2. 변수 = [] # 배열선언해서 append()로 배열에 값을 넣는다.
        3. 메서드 자체에 출력문이 있는데, 이것을 다시 출력문으로 감싸면 None값이 출력되기도 한다.
    예외처리(Python_Except.py)
        1. 예외 처리 문법
            try: 
                실행명령문1
            except 에러 종류1:
                예외 처리 명령문1
            (catch부분을 except으로 작성하는듯 싶다.)
        2. 에러 종류를 지정할수도 있지만 Exception으로 지정하면 모든 예외를 처리가능하다.
        3. 에러 종류뒤에 as err를 작성함으로써 발생한 에러가 어떤 에러인지 출력 할 수도 있다.
    에러발생시키기(Python_Except_Raise.py)
        1. 에러 발생시키기 문법
            raise 에러종류
            (raise뒤에 에러종류를 입력해두면 해당 에러가 강제적으로 에러를 발생시킨다.)
    사용자 정의 예외처리(Python_Except_Custom.py)
        1. 사용자 정의 예외처리를 사용하고 싶다면, 새롭게 만들 예외의 클래스를 만들어서 Exception을 상속 받아 정의 하면 된다.
    파이널(Python_Except_Finally.py)
        1. try except 구문을 진행한 후 반드시 실행되는 부분이 finally부분이다.
    퀴즈9(Python_Quiz9.py)
        예외 처리에 대해서 복습을 할 수 있는 예제 

2021년 9월 10일 
    메소드 오버라이딩(Python_Method_Overriding.py)
        1. 부모 클래스에 있는 메서드를 자식클래스에서 새롭게 재정의하여 사용하는 것
    패스(Python_Pass.py)
        1. 함수뿐만아니라 if, for, while등에서도 pass를 사용하여 당장의 세부 동작을 정의 하지 않은 채 둿다가 나중에 다시 코드를 완성하도록 할 수 있다.
    슈퍼클래스(Python_Super.py)
        1. 부모클래스의 이름을 직접 적지않고 super()를 사용하여 부모클래스에 접근이 가능하다.
        2. super()클래스를 사용한 경우에는 self를 제외한다.
        3. 상속받은 클래스가 다수 있고, 각 부모클래스에 각각 접근하고자 할때는 부모클래스의 이름을 적고 접근해야한다.
        4. 상속받은 클래스가 다수 있고, super()를 사용한 경우에는 제일 먼저 상속 받은 부모클래스에 접근하게된다.
    슈퍼클래스 설명코드(Python_Super_Exam.py)
        1. 슈퍼클래스(Python_Super.py)에서 공부한 3, 4 내용을 이해하기 위한 코드작성 
    스타크래프트 전반(Python_Starcraft_FirstHalf.py)
        1. 각 클래스별 공통기능에 대하여 생각해보고 어떻게 상속하여 각 유닛 클래스까지 만드는 과정을 생각해보는 시간!
    스타크래프트 후반(Python_Starcraft_SecondHalf.py)
        1. 스타크래프트 전반(Python_Starcraft_FirstHalf.py)을 활용하여 만들어둔 클래스를 어떻게 활용해야 하는지 공부하는 시간!
        2. 만들어둔 유닛들을 일괄관리를 하고싶으면 리스트에 넣어서 사용가능하다 
            변수명 = []
            변수명.append(유닛변수)
        3. 동시 명령
            for 각변수 in 리스트변수:
                각변수.명령함수
        4. isinstance(변수명, 인스턴스명) 
            출력값은 boolean값이며, 변수가 인스턴스일 경우 True를 반환한다.
            리스트에 다양한 인스턴스가 들어가 있는 경우에 각각을 제어 하기에 좋다.

2021년 9월 9일
    다중상속(Python_Multi_Inherit.py)
        1. 상속은 하나의 부모만을 받는 것이 아닌 여러 부모클래스를 상속받아 사용가능하다.
        2. 문법  ->  class 자식클래스(부모클래스1, 부모클래스2, ...):

2021년 9월 7일
    생성자(Python_Init.py)
        1. __init__함수는 사용자가 따로 호출하지 않아도 클래스 객체를 생성할 때 자동으로 호출된다.
        2. 객체를 생성할 때는 이 생성자의 전달 값에 해당되는 갯수 만큼 값을 던져야한다.
        3. slef를 제외하고 나머지 파라미터를 전달한다.
        4. 여러 객체를 생성할 때 각각의 정해진 파라미터 갯수 만큼 전달해야한다.
    맴버변수(Python_Member_Variable.py)
        1. 클래스 내에 정의된 변수를 맴버변수라고 하며, self.와 함께 사용할 수 있다.
        2. Unit 클래스 경우 name, hp, damage가 맴버변수가 된다.
        3. 객체를 생성 후 객체의 맴버변수를 추가 가능하다.
    메소드(Python_Method.py)
        1. 클래스 내에서 정의되는 함수를 메소드라고 부른다.
        2. __init__으로 클래스의 객체를 생성한 뒤 이 객체의 동작을 정의 한것이 메소드라 생각할수있다.
            예) 유닛생산 : 객체 생성, 유닛 이동(공격) : 메서드
    상속(Python_Inherit.py)
        비슷한 기능을 가지고 있는 기능을 하나로 합쳐서 부모클래스를 만들어 상속시키면 중복된 맴버변수는 정의 하지 않아도 된다.
        재활용이 가능하다는점에서 상속을 이용한다. 

2021년 9월 6일     
    With(Python_With.py)
        1. 기존의 파일 입출력 형식을 기준으론 파일열기, 파일데이터작업, 파일닫기의 공정을 한번에 처리가능하게 간소화시킨다.
        2. with 문법
            with 작업 as 변수명:
                실행명령문1
                실행명령문2
           예) 
            with open("x.txt","w",encoding="utf8") as tt
                tt.write("txt추가")
    퀴즈7(Python_Quiz7.py)
        반복문과 함께 다양한 출력포멧을 복습해보았다.
    클래스(Python_Class.py)
        1. 동일한 내용의 코드를 반복적으로 사용해야 할 경우에 클래스를 활용한다.
        class 클래스명:
            def 메소드1(self, 전달값1, 전달값2,...):
                실행명령문1
                실행명령문2
            def 메소드2(self, 전달값1, 전달값2,...):
                실행명령문1
                실행명령문2
        2. 클래스를 통해서 만들어지는 것을 객체(Object)라 표현하며, 이 객체는 클래스의 인스턴스(Instance)가 된다.

2021년 9월 5일
    피클(Python_Pickle.py)
        1. 일반적인 프로그램은 내부적인 데이터가 어떤 식으로 처리가 되는지 알기가 어렵다. 그렇기에 중간 데이터, 최종 데이터등을 파일로서 저장 하여 보관한다. 
        2.  pickle의 경우는 일반적인 txt파일과 다르게 한글, 영어, 숫자등의 내용을 담는 것이 아닌 .jpg, .png, .mp3, .exe등과같은 바이너리 파일을 저장한다.
        3. pickle파일 작성, 수정, 일기 작업시 사용되는 open()함수 이용시 일반 파일입출력과 비슷하지만 열기모드에 'b'를 추가해서 작성해준다. 예)'wb'
        4. 일반파일 입출력과는 다르게 데이터네 한글이 포함되더라도 별도의 인코딩 지정은 안해도 된다.
        5. pickle을 이용하여 데이터를 파일로 저장할시에는 pickle.dump() 를 이용한다. 
            사용법) pickle.dump(저장할데이터,데이터를_저장할_파일)
        6. pickle파일의 데이터를 읽고싶을경우 pickle.load()를 이용한다.

2021년 9월 4일
    퀴즈6(Python_Quiz6.py)
        1.지금까지 공부한 함수에 관한 기본지식, 조건문에 대한 내용, 반올림함수(round())에 대해 복습하는 문제
        2. 출력문의 각종 기술 방법에 대해 복습
    숫자 처리 함수 재기재(Python_Math_Equation.py)
        1. 반올림 함수 round()의 기능을 기존에는 실수를 정수로 반올림하는 기능이라고 공부하였지만 파라미터를 하나더 추가함으로 반올림후 표기할 자리수를 지정할수 있음을 추가하였다.
        round(값, 표기할 자릿수) #음수도 가능 
    표준 입출력(Python_Standard_Input_Output.py)
        1. 표준 출력
            a. 문자열 구분짓는 방법을 정의 (sep옵션)
                print("Python","Java",sep=",")
            b. 출력문 줄 바꿈 방지 옵션 (end옵션)
                print("Python",end="?")
                print("Java")
            c. sys모듈(file=sys.stdout, file=sys.stderr)
                일반적인 경우와 에러의 경우로 구분지어 로그 출력시 빠른 대응이가능 하다고 하던데 현시점으로는 이런기능도 있다에서 끝
            d. 문자열 편집함수 ljust(x), rjust(x)
                사용 예) 문자열.ljust(3), 문자열.rjust(6)
                문자열 출력시 설정한 x개 만큼의 빈공간을 확보후 l, r로 기준위치에서부터 값을 채운다.
            e. 문자열 편집함수 zfill(x)
                사용 예) 문자열.zfill(3)
                문자열 출력시 설정한 x개 만큼의 빈공간을 확보한후 값을 대입후 빈공간에 대하여 0을 채워 넣는 방식
        2. 표준 입력
            input() 함수로 값을 입력받아 변수에 대입하는 경우 이 변수는 무조건 문자열 형태의 변수가 된다. 입력받는 데이터가 숫자형으로 입력을 받아 계산까지 필요한 경우에는 int()로 형 변환을 시켜주어야 한다.
    다양한 출력포멧(Python_Output_Format.py)
        다양한 출력포멧을 {}안에 넣어서 사용할 수 있다.
            {인덱스 : [[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}
        예시) print("{0:^>+10,.2f}".format(10000/8))
            {}의 내용 설명
            1. 0  :  인덱스 값
            2. :  :  출력 포멧을 지정하겠다는 구분자 
            3. ^  :  빈 공간은 ^로 채우기(공백도 가능)
            4. >  :  > 오른쪽정렬, < 왼쪽정렬
            5. +  :  +,- 구분없이 하나를 사용하면 부호를 포함한 출력
            6. 10 :  공간확보의 크기 (10칸 확보)
            7. ,  :  1000단위로 , 구분자를 사용하여 출력
            8. .2 :  소수점 둘째자리로 출력(f가 없다면 지수형태로 출력한다.)
            9. f  :  소수점 형식으로 출력
    파일입출력(Python_File_Input_Output.py)
        1. 프로그래밍에서 파일을 다룰 떄 순서
            a. 파일을 연다
            b. 파일에 내용을 작성하거나 읽는다.
            c. 파일을 닫는다.
        2.  파일을 열기 위한 함수 open()
            기본구성 : open("파일명", "열기 모드",encoding="인코딩")
                1) 파일명 : 조작을 하고자하는 파일의 이름
                2) 열기모드의 종류
                    a. 읽기(read,"r") : 파일의 내용을 읽어오는 기능
                    b. 쓰기(write, "w") : 파일에 어떤내용을 쓸 때 사용 동일한 파일명이 없을 경우 새로 만들고, 있을 경우 그 파일을 덮어쓰게 되므로 기존 내용은 삭제 된다.
                    c. 이어쓰기(append, "a") : 그 파일의 맨 밑에 이어서 쓴다.
                3) encoding 일반적으로 utf8로 설정해 주면 한글을 포함한 내용을 다룰때 문제가 없다.
        3. 파일의 내용을 읽어올때 파일 데이터를 읽어오는 함수
            a. 파일명.read() : 파일의 전체 데이터를 읽어온다.
                예) print(파일명.read())
            b. 파일명.readline() : 파일의 한 줄씩 데이터를 읽어온다.
                readline()함수에는 줄 바꿈을 포함하고 있기에 end=""을 추가 작성하는 것이 좋다.
                예) print(파일명.readline(), end="")
        4. 한 줄씩 읽어오는 함수로 전체 데이터를 출력할 경우 (반복문 while)
            line변수(string형)에 파일명.readline()로 한 줄씩 담아 출력하되, if not line: 에서와 같이 더 이상 읽어올 내용이 없을 때 반복문을 탈출한다.
        5. 한 줄씩 읽어오는 함수로 전체 데이터를 출력할 경우 (반복문 for)
            lines변수(list형)에 파일명.readlines()로 리스트 형태로 모든 줄을 담아
            한 줄씩 출력한다.
            
2021년 9월 3일
    함수(Python_Function.py)
        함수를 정의하여 사용 방법에 대하여 공부
        기본 구조
            def 함수이름():
                실행 명령문1
    함수의_파라미터_리턴값(Python_Function_Input_Output.py)
        함수를 정의할 때 파라미터, 리턴값을 설정가능하다.
        이 때 튜플의 형식으로도 리턴값을 줄 수도 있다.
    기본값 설정(Python_Default_Value.py)
        함수정의 할 때, 파라미터에 초기값을 설정하면 함수를 사용시 초기값이 있는 파라미터에는 값을 설정하지 않아도 기본값으로써 함수가 출력된다.
        예시)
            def profile(name, age, main_lang):
            print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    키워드인자(Python_Keyword_Factor.py)
        순서에 구애받지 않으면서, 기본 값을 쓰고 필요한 부분만 콕 찍어서 값을 전달 할 경우 사용한다.
        예시)
            def profile(name, age, main_lang):
            print(name, age, main_lang)
            profile(name = "유재석", main_lang="파이썬", age = 20) # 유재석씨(20세)의 주 사용 언어는 파이썬
    가변인자(Python_Variable_Factor.py)
        1. 일반 함수 작성방법은 동일.
        2. 파라미터를 가변인자로 사용하고 싶을 경우에는 파라미터 앞에 * 를 추가한다.
        3. 가변인자의 경우는 배열로써 취급하여 실행명령문을 작성한다.
                # print(type(language)) #tuple
                for lang in language:
                    print(lang,end=" ") #언어들을 모두 한 줄에 표시
               print() # 주바꿈 목적
    지역변수,전역변수(Python_Local_Global_Variable.py)
        전역변수 : 함수 밖에 정의 된 변수
        지역변수 : 함수 내부에 정의 된 변수

2021년 9월 2일 
    퀴즈5(Python_Quiz5.py)
        랜덤함수, 반복문, 조건문의 사용방법에 대해 생각해볼수 있는 문제.

2021년 8월 29일
    조건문if(Python_If.py)
        1. 조건문 if를 사용할 경우에는 if를 기준으로 공백(스페이스) 4칸씩 들여쓰기를 해야한다.
        2. 조건 뒤에는 :을 붙여준다.
            문법 -> if 조건:
                       출력문
        3. 들여쓰기를 하는동안엔 조건문의 출력문이 된다.
        4. else if 를 줄여서 elif로 작성한다.(이외의 조건 elif는 여러번 사용 가능하다.)
        5. 어느 조건에도 만족하지 않는 값을 출력할 때는 else로 출력.
    반복문for(Python_For_Loop.py)
        1. for문의 문법 
            for문 최후방에 :을 작성한다.
            for 변수 in 반복대상:
                실행명령문1
        2. if문과 동일하게 for문에서 실행 코드는 들여쓰기이후 작성한다.
    반복문while(Python_While_Loop.py)
        1. while문의 문법
            while boolean
                실행명령문1
        2. boolean가 false일때까지 반복문을 실행
    반복문제어(Python_ContinueBreak.py)
        1. continue
            더 이상 아래 명령들을 실행하지 않고 다음 반복 대상으로 넘어갈 경우 사용
        2. break
            즉시 반복문을 탈출하는데 사용
    한줄반복문for(Python_ForOneLoop.py)
        1. 한 줄 for문의 예시
            정의하고자하는변수명 = [실행명령문 for 집합(배열)에서 한개씩 습득하여 임시저장할 변수명(i) in 가공할변수명]
            단순한 반복문의 경우 한줄 for을 이용하는 것도 좋다.

2021년 8월 23일
    사전(Python_Dictionary.py)
        1. 사전형
            자바의 해시맵과 비슷하게 key와 value로 이루어진 자료구조이다.
            key와 value는 콜른(:)으로 구분된다.
            두 개 이상의 데이터를 저장할 경우에는 콤마(,)를 사용해서 구분짓는다.
                예) {key1 : value1, key2 : value2}
            이 때 key들은 중복 값을 허용하지 않는 유일한 값으로 설정해야 한다.
        2. 키 값을 출력
            1) 사전형변수[키값] 
                특징 : 없는 키 값을 검색시 프로그램이 중단
            2) 사전형변수.get(키값)
                특징 : 없는 키 값을 검색시 프로그램을 중단하지 않고 None을 출력
        3. 사전형변수.get(키값, "기본값설정")
            get함수를 사용할 경우에는 키값이 설정되지 않는 경우는 기본값을 출력한다.
        4. 데이터를 검색하는 방법(결과값  boolean값)
            검색키값 in 사전형변수
        5. 데이터의 업데이트 또는 추가 
            사전형[키값] = "벨류값"
                키값이 설정되어 있다면 벨류값이 재설정
                키값이 설정되어 있지 않다면 데이터 추가
        6. 데이터 삭제
            del 사전형변수[키값]
                해당 키값의 데이터를 삭제
        7. 현재 사용중인 key값을 전부 출력
            사전형변수.keys()
        8. 현재 사용중인 value값을 전부 출력
            사전형변수.value()
        9. 현재 사용중인 key, value값을 쌍으로 출력
            사전형변수.value()
    튜플(Python_Tuple.py)
        1. 리스트의 읽기 전용 버전(변경, 추가, 삭제가 불가)
        2. 리스트는 대괄호[]로 하지만 튜플은 소괄호()로 선언한다.
    세트(Python_Set.py)
        1. 수학에서의 집합과 비슷한 자료구조, 중괄호{}를  이용하여 선언할 수 있다.
        2. 중복을 허용하지 않으므로 같은 값은 여러번 적어도 딱 한 번만 들어간다(자동중복 제거) 
        3. 값을 선언하는 방법
            세트변수 = {값, 값, 값}
            세트변수 = set([값, 값])
        4. 교집합 
            세트변수1 & 세트변수2
            세트변수1.intersection(세트변수2)
        5. 합집합
            세트변수1 | 세트변수2
            세트변수1.union(세트변수2)
        6. 차집합
            세트변수1 - 세트변수2
            세트변수1.difference(세트변수2)
        7. 세트의 데이터 추가
            세트변수1.add(값)
        8. 세트의 데이터 제거
            세트변수1.remove(값)
    자료구조의 변경
        1. type()을 이용하여 해당 변수의 타입을 확인 가능한다.
        2. 리스트[], 튜플(), 세트{} 서로 타입변경이 가능하다.
        3. string, int쪽도 type()로 타입을 확인가능하다.
    간단한 퀴즈4
        1. 리스트의 순서를 랜덤으로 바꿔주는 shuffle(리스트변수)
        2. sample(리스트변수, 갯수)

2021년 8월 19일
    문자열 포멧(Python_String_Format.py)
        1. 단순한 문자열 연결
            "문자열1" + "문자열2" = "문자열1문자열2"
            "문자열1", "문자열2" = "문자열1 문자열2"
        2. %를 이용한 방법
            %d 는 정수를 표현
            %c 는 문자를 표현
            %s 는 문자열을 표현(거의 만능)
        3. .format()을 이용한 방법
            출력문에 넣고 싶은 부분에 {}으로 설정, {}안에 들어갈 값으로 % 뒤에 값을 지정해준다. print("{}" % "지정값")
        4. 이름으로 지정하는방법
            형식은 3번의 .format()과 동일하나 {}내부에 이름을 지정해주고 .format(이름 =값)을 지정해준다.
        5. f-string방법
            변수를 이용한 방법으로 print(f"문자열 {변수명}")으로 문자열은 그냥 출력되고 {}내부의 변수에 지정된 값이 출력된다.
    탈출문자(Python_String_Escape.py)
        1. \n 줄바꿈 
        2. \" 따옴표출력
        3. \\ 역슬래시 출력
        4. \r 커서를 맨앞으로
        5. \b 백스페이스 
        6. \t 탭
    간단퀴즈(Python_Quiz3.py)
        문자열 조작을 깊게 생각해 볼수 있는 문제.
        1. 슬라이싱        예)  문자열[:] 
        2. 문자열 위치찾기   예)  문자열.find(문자)
        3. 문자의 길이      예) len(문자열)
        4. 문자 사용횟수    예) 문자열.count(문자)
    리스트(Python_List.py)
        1. 리스트 선언      :   변수명 = [값, 값, 값] #같은 타입끼리만으로 선언안해도 된다.
        2. 인덱스 값 추출   :   문자열.index(값)
        3. 리스트에 값 추가  :   문자열.append(값)
        4. 원하는 위치에 값 추가 : 문자열.insert(추가할 위치,값)
        5. 뒤에서부터 하나씩 제거 : 문자열.pop()
        6. 리스트에 같은값이 몇개인지 : 문자열.count(값)
        7. 오름차순 정렬 : 문자열.sort()
        8. 내림차순 정렬 : 문자열.reverse()
        9. 리스트 데이터 없애기 : 문자열.clear()
        10. 리스트 확장 : 문자열.extend(다른 리스트)

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

  
