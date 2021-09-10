# 에러 발생시키기

# 의도적으로 에러를 발생시큰 ㄴ방법
# 자바나 C# 등에서 사용했던 throw와 같은 기능이라 생각하면 좋다.

# 에러 발생 문법
# raise 에러 종류

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))   
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    if nums[0] >= 10 or nums[1] >= 10: # 입력받은 수가 한자리인지 확인
        raise ValueError # 강제로 값이 잘못되었다는 에러를 발생
    nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:  # ValueError : 값이 잘못되어서 발생하는 에러.
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # ZeroDivisionError : 0으로 나눗셈을 할 경우 발생하는 에러.
    print(err)
except Exception as err: # 원인을 예측하지 못 한 에러를 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
