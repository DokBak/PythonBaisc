# 예외 처리

# 설계대로 작성된 처리가 진행되지 않을 경우를 대비한 처리

# 예외 처리 문법
# try:
#     실행명령문1
#     실행명령문2
# except 에러 종류1:
#     예외 처리 명령문1
#     예외 처리 명령문2
# except 에러 종류2:
#     예외 처리 명령문1
#     예외 처리 명령문2


# 에러가 발생하면 해당 에러의 종류를 확인 가능하다.
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))   
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:  # ValueError : 값이 잘못되어서 발생하는 에러.
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # ZeroDivisionError : 0으로 나눗셈을 할 경우 발생하는 에러.
    print(err)
except Exception as err: # 원인을 예측하지 못 한 에러를 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
