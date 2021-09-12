# 파이썬 개발시에는 유용한 패키지가 많다.

# 그렇지만 패키지를 찾아보자
# https://pypi.org

# 사이트에 접속하여 검색창 밑에 browse projects를 클릭 하면 좌측에 주제별 패키지를 볼수있는 트리가 존재하여 원하는 검색가능하다.
# 이번 실습에서 사용하기 위한 패키지 BeautifulSoup를 검색하여 나온 패키지를 다운로드한다.
# 다운로드할 패키지 : beautifulsoup4 4.10.0

# 다운로드 방법은 원하는 패키지를 클릭해 사이트에 있는 Copy to clipboard를 클릭한 뒤 VS Code의 터미널쪽에서 마우스 우클릭을 통해 붙여넣기하여 설치한다.
# 패키지 설치시 붙여넣기할 메시지 
# pip install [패키지]

# 공식 홈페이지에서 파이썬을 설치한 경우에는 pip를 검색하지 못할경우가 있다 
# homebrew 패키지 관리자를 이용하고 있을 경우에는 brew 명령어를 통해 pip를 설치해주어야 한다.

# ------------------ Python_Package_Search.py에서 연습을 하기위해서 [pip install beautifulsoup4]를 터미널에서 입력

# 패키지의 Quick start의 처음 3문장을 붙여넣기 한다.
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# pip 명령은 패키지 설치 외에도 다양한 명령이 있다.
# install           : pip install [패키지]              : 패키지 설치
# install --upgrade : pip install --upgrade [패키지]    : 패키지 업그레이드
# uninstall         : pip uninstall [패키지]            : 패키지 삭제
# list              : pip list                         : 설치 패키지 목록
# show              : pip show [패키지]                 : 패키지 상세 정보