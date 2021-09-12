# All 

# import 를 사용할때 * 를 사용함으로써 해당 모듈이나 패키지에 있는 모든 것을 가져다 사용하겠다는 의미이다.

from travel import *
trip_to = vietnam.VietnamPackage() # 베트남
trip_to.detail()

trip_to = thailand.ThailandPackage() # 태국
trip_to.detail()

# * 을 쓴다는 것은 travel이란 패키지에 있는 모든 것을 가져다 쓰겠다는 의미인데 패키지를 만든 사람이 공개 범위를 설정해줄 수 있다.
# 패키지에 포함된 모듈 중에서 import되기를 원하는 것만 공개를 하고 나머지는 비공개로 둘 수가 있다.

# __init__.py 에 __all__이라는 변수에 리스트 형태로 공개하려는 모듈 이름을 추가하면 해당 모듈에 대해 공개 설정을 할 수 있게 된다.
# all 앞 뒤로 밑 줄은 2번씩 적어주어야 한다. __all__ 이런식으로

