
# 피클

# 일반적으로 프로그램을 기동시켜 작성되거나 수정된 데이터의 경우에는 프로그램이 종료됨에 따라 데이터가 흔적도 없이 사라지게 된다.
# print()라는 것으로 터미널에 어떤 데이터가 어떤식으로 처리가 되는지까지는 확인 할 수 있지만,
# 처리과정에서 발생한 데이터를 그대로 가져와 재사용을 할 수 있는 방법은 없다.
# 그렇기에 이전에 공부하였던 파일 입출력으로 파일에 데이터를 읽거나 쓰는 작업을 통해 데이터를 보존 하기도 한다.
# pickle이라고 하는 것은 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하거나 불러올 수 있게 해주는 모듈입니다.


# pickle의 특징 
# 1. pickle을 이용해서 저장되는 파일은 텍스트(txt)가 아닌 바이너리(binary) 형태이다.
#   일반적으로 한글, 영어, 숫자등의 내용을 담고 있는게 텍스트 파일
#   .jpg, .png와 같은 이미지나 .mp3와 같은 음악 또는 .exe와 같은 실행 파일 등이 바이너리 파일
# 2. open()함수 이용시 파일입출력에서 공부한 열기모드에서 모드 뒤에 'b'를 추가해 주어야 한다.
#   예를들어 'wb'로 작성해 주어야 한다.
# 3. open()함수 이용시 데이터 내에 한글이 포함되어 있다 하더라도 별도의 encoding은 지정할 필요가 없다.

# pickle을 이용하여 데이터를 파일로 저장을 할 때는 dump() 함수를 사용
# dump()의 구조
# dump(저장할_데이터, 데이터를_저장할_파일)
print("-----pickle모듈을 사용함에 있어서 임포트를 먼저 해주어야 한다.-----")
import pickle # pickle 모듈 가져다 쓰기

print("-----저장할 파일과, 저장할 데이터 생성-----")
profile_file = open("profile.pickle","wb") # 바이너리(binary) 형태로 저장
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구","골프","코딩"]}

print("-----저장할 파일과, 저장할 데이터 확인-----")
print(profile)

print("-----저장할 파일에 저장할 데이터 저장 -----")
pickle.dump(profile,profile_file) #profile데이터를 file에 저장

print("-----파일 닫기-----")
profile_file.close()

# pickle을 이용하여 파일의 데이터를 읽어올때는 load() 함수를 사용
# load()의 구조
# load(읽어올 파일) 
print("-----읽을 파일 지정-----")
profile_file = open("profile.pickle", "rb") # 읽을 때에도 바이너리(binary) 명시

print("-----읽기로 지정된 파일의 데이터를 불러와 profile변수에 넣기-----")
profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장

print(profile)
print("-----파일 닫기-----")
profile_file.close()