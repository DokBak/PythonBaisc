# 가변 인자

# 가변 인자란 말 그대로 변할 수 있는 인자를 의미한다.
# 예)
# 유재석과 김태호가 사용가능한 언어의 갯수가 각각 5개, 2개 일 경우.


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름:{0}\t나이:{1}\t".format(name, age), end= " ") # 문장 출력 후 줄 바꿈 대신 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석",20, "Python", "Java", "C", "C++", "C#")
profile("김태호",25,"Kotlin","Swift","","","")

# 파라미터가 다수 사용 될 경우에 해당 변수를 전부다 일일이 작성 하는 고된 작업이 된다.
# 일반 함수에서는 파라미터의 갯수가 고정되어있지만 함수의 파라미터의 갯수가 가변으로 설정하는 방법
# (약간은 다르겠지만 배열(?)처럼 데이터갯수가 고정되있지않고 ArrayList처럼 데이터 저장공간이 정해지지 않았다는 점이 비슷)

print("-----가변인자함수-----")
# 가변인자사용 함수 구성
# def 함수이름(전달값1, 전달값2, ... , *가변인자)
#   실행 명령문1
#   실행 명령문2
#   ...
#   return 반환값

# 가변 인자는 앞에 *표시를 하나 추가해주면 된다.

def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ")

    # print(type(language)) #tuple
    for lang in language:
        print(lang,end=" ") #언어들을 모두 한 줄에 표시
    print() # 주바꿈 목적

profile("정형돈", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") #JavaScript
profile("정준하", 20, "Kotlin", "Swift")