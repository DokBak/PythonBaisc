# 사용자 정의 예외처리

# 사용자 정의 예외처리를 사용하고 싶다면, 새롭게 만들 예외의 클래스를 만들어서 Exception을 상속 받아 정의 하면 된다.

class BigNumberError(Exception): # 사용자 정의 에러 
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "[에러 코드 001]" + self.msg # 에러 메시지 가공

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))   
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    if nums[0] >= 10 or nums[1] >= 10: # 입력받은 수가 한자리인지 확인
        raise BigNumberError("입력값 : {0}, {1}".format(nums[0],nums[1])) # 자세한 에러 메시지
    nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:  # ValueError : 값이 잘못되어서 발생하는 에러.
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # ZeroDivisionError : 0으로 나눗셈을 할 경우 발생하는 에러.
    print(err)
except BigNumberError as err: # 사용자 정의 예외 처리
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 에러 메시지 출력
except Exception as err: # 원인을 예측하지 못 한 에러를 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
