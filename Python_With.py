#  with

# 파일입출력 작업을 진행 할 경우에 파일을 가지고 작업할시  open()작업 뒤에는 반드시 close()함수를 통해 닫아주어야 한다.
# 이 close() 작업을 잊어버리지 않도록 하는 도와주는것이  with

# with 구문
# with 작업 as 변수명:
#   실행명령문1
#   실행명령문2


print("-----With 이용하기-----")
import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

# Python_pickle.py에서 작성한 pickle파일의 데이터가 아래와 같이 출력된다.
# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부합시다.")
# 파이썬을 열심히 공부합시다.


print("-----파일 입출력 with 사용 -----")
with open("study.txt","r",encoding="utf8") as study_f:
    print(study_f.readline())

with open("study.txt","a",encoding="utf8") as study_t:
    study_t.write("with문을 이용한 추가데이터")


print("-----기존 파일입출력 방식 확인-----")

print("-----파일 입출력 파일 읽기 연습-----")
filetest1 = open("study.txt","r",encoding="utf8")
print(filetest1.readline())
filetest1.close()

print("-----파일 입출력 파일 쓰기 연습-----")
filetest2 = open("study.txt","a",encoding="utf8")
filetest2.write("\n자바도 열심히 공부합시다.")
filetest2.write("\nC언어도 열심히 공부합시다.")
filetest2.close()

print("-----파일 입출력 파일 읽기 연습-----")
filetest3 = open("study.txt","r",encoding="utf8")
print(filetest3.readline(),end="")
print(filetest3.readline(),end="")
print(filetest3.readline())
filetest3.close()


print("-----다시 이번 공부 문법 with-----")
with open("study.txt","r",encoding="utf8") as test:
    print(test.read())
