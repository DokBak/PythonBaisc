# 패키지

# 여러 모듈들을 모아 놓은 집합을 패키지라한다. 패키지는 하나의 폴더 안에 여러 모듈 파일들로 구성된다.

#import를 할 때는 그 대상이 모듈이나 패키지여야 한다. 클래스나 함수를 import하는것은 불가능하다.
import travel.thailand # (O)
# import travel.thailand.ThailandPackage #(X)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

import travel.vietnam
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()