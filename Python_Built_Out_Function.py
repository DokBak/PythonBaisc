# 외장 함수

# 내장 함수와 달리 import를 해야하는 모듈을 의미한다.
# 자세한 내용은 구글에 list of python modules로 검색해서 나온 공식사이트에서 확인 가능하다.
# 사이트 : https://docs.python.org/3/py-modindex.html



import glob
print(glob.glob("*.py")) # 작업 공간내에 존재하는 확장자가 py인 모든 파일을 출력

import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder): # 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
else: # 폴더가 존재하지 않는다면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) #  glob모듈의 glob()함수와 비슷하게 현재 작업 디렉토리 내의 폴더와 파일 목록을 출력해준다.

import time
print(time.localtime()) # 뭔가 알아보기 힘들게 나오는 시간함수

print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초 
# 현재 시간이 출력된다                  2021-09-13 01:39:19

import datetime
print("오늘 날짜는", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print(td)
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후