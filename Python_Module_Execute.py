# 모듈 직접 실행

# 모듈이 직접 실행되는지, 아니면 별도의 파일에서 호출되어 실행되는지는 이렇게 구분된다.
# __name__, __main__ 

# if __name__ == "__main__": # 직접 실행되는 경우
#     pass
# else: # 외부에서 호출되어 실행되는 경우
#     pass 

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()