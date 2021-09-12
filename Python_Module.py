# 모듈

# 랜덤함수를 사용하기위해 다음과 같이 코드를 입력해왔었다.
# import ~
# from ~ import *
# 여기서 random이 모듈을 의미했다.
# C#을 기준으론 dll과 같은 역할
# 자주 사용할 것 같은 기능은 모듈로 만들어 사용하면 좋다.

# 직접 만든 모듈을 사용할 때는 작성중인 파일과 모듈로 사용할 파일이 같은 경로상에 있어야한다.

# 기본 사용법
# import theater_module # theater_module 을 가져다가 사용
# theater_module.price(3) # 3명이 영화를 보러 갔을 때 가격 
# theater_module.price_moring(4) # 4명이 조조 영화를 보러 갔을 때 가격
# theater_module.price_soldier(5) # 군인 5명이 영화를 보러 갔을 때 가격

# 별명 설정
import theater_module as mv # theater_module 을 새로운 별명인 mv로 사용 
mv.price(3) # 3명이 영화를 보러 갔을 때 가격 
mv.price_moring(4) # 4명이 조조 영화를 보러 갔을 때 가격
mv.price_soldier(5) # 군인 5명이 영화를 보러 갔을 때 가격

# form ~ import 구문 사용법 
# from theater_module import * # theater_module 내에서 모든 것을 가져다가 사용
from theater_module import price,price_moring as price
price(3) # theater_module. 필요없음
# price_moring(4)
# price_soldier(5) # 모든 함수를 사용하겠다는 *를 사용하지 않고 사용할 함수만 기술할 수도 있다.
# from ~ import의 구문에도 as로 별명을 사용 할 수 있다.