# 파일입출력

# 프로그래밍에서 파일을 다룰때에는 일반적으로 
# 1. 파일을 연다.
# 2. 파일에 어떤 내용을 쓰거나 읽는다.
# 3. 파일을 닫는다.
# 의 순서로 진행된다.

# 1. 파일을 열기 위한 함수 open()
# open("파일명", "열기 모드",encoding="인코딩")
# 1) 파일명 : 조작을 하고자하는 파일의 이름
# 2) 열기모드의 종류
#   a. 읽기(read,"r") : 파일의 내용을 읽어오는 기능
#   b. 쓰기(write, "w") : 파일에 어떤내용을 쓸 때 사용 동일한 파일명이 없을 경우 새로 만들고, 있을 경우 그 파일을 덮어쓰게 되므로 기존 내용은 삭제 된다.
#   c. 이어쓰기(append, "a") : 그 파일의 맨 밑에 이어서 쓴다.
# 3) encoding 일반적으로 utf8로 설정해 주면 한글을 포함한 내용을 다룰때 문제가 없다.

# 파일을 오픈할때 파일의 경로는 소스파일의 경로와 동일하다.
print("-----터미널이 아닌 파일에 데이터 쓰기(파일이 없는 경우 생성)-----")
score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기("w")모드로 열기
print("수학 : 0",file = score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50",file = score_file) # score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기
# 파일의 close()는 반드시 해주어야 한다.

# 파일에 데이터를 추가할때 print(입력값, file= 파일명)이외의 방법
print("-----파일에 데이터를 추가하는 다른 방법-----")
score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일을 쓰기("a") 모드로 열기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close() # score.txt 파일 닫기

# 파일의 정보를 가져오기 : read() : 파일 전체 읽기
print("-----파일의 전체 데이터 읽어오기-----")
score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
print(score_file.read()) # 파일 전체 읽어오기
score_file.close()

# 파일의 정보를 가져오기 : readline() : 파일 한 줄 읽기
# readline()함수의 경우 줄바꿈을 포함하고 있기에 end=""을 포함해주는 것이 좋다.
print("-----파일의 한 줄만 읽어오기-----")
score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
print(score_file.readline(),end="") # 파일 한 줄 읽어오기
print(score_file.readline(),end="") # 파일 한 줄 읽어오기
print(score_file.readline(),end="") # 파일 한 줄 읽어오기
print(score_file.readline(),end="") # 파일 한 줄 읽어오기
score_file.close()

# 파일의 모든 데이터를 출력할 때 반복문 while을 사용한다면 
# line변수(string형)에 한줄을 담고, 출력하고, 같은 변수에 새로운 다음 줄을 담고 출력하고 와 같은 형태로 출력한다.
# 이때 line 변수에 담기는 것은 [score_file.readline()] 이며, readline()이다. 
print("-----파일의 줄 수를 모르기에 반복문 while로 모든 줄을 출력하기-----")
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어올 내용이 없으면?
        break # 반복문 탈출
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
score_file.close()


# 파일의 모든 데이터를 출력할 때 반복문 for을 사용한다면 
# lines변수(list형)에 모든 줄을 담고 -> 이때 담는 형태는 [score_file.readlines()]
# line 변수에 한 줄씩 호출하여 출력한다. -> 이때 줄바꿈 중복 중복 작업을 추가해 주어야한다.
print("-----파일의 줄 수를 모르기에 반복문 for로 모든 줄을 출력하기-----")
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()