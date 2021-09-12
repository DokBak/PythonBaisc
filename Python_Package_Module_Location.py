# 패키지와 모듈 위치

# 패키지나 모듈은 호출을 하려는 파일과 동일한 경로에 있거나 또는 파이썬 라이브러리들이 모여 있는 폴더에 있어야 사용이 가능하다.
# 파이썬에서 사용하려는 모듈이 어느 경로에 있는지 확인 할 수 있는 방법이 있다.

import inspect
import random
from travel import thailand
print("inspect.getfile(random) : " + inspect.getfile(random)) # random 모듈의 위치
    # 기존경로 : /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/random.py
print("inspect.getfile(thailand) : " + inspect.getfile(thailand))
    # 기존경로 : /Users/jonmingi/Desktop/DokBak/PythonBaisc-1/travel/thailand.py

# random모듈이 있는 lib에 travel을 복사해 넣으면 기본모듈처럼 사용가능하다.