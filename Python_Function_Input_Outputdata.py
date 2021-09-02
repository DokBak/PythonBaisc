# 함수 전달값, 반환값

# 이전의 함수 예제에서는 전달값과 반환값이 없는 함수를 이용하였는데 
# 이번에는 전달값과 반환값이 있는 함수를 작성한다.
# 전달값은 parameter(매개변수), 반환값은 return 


# 함수의 동작을 정의 
# def 함수이름(전달값1, 전달값2):
#  실행 명령문1
#  실행 명령문2
#  return 반환값1, 반환값2

print("----- deposit(입금)테스트 -----")
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 입금 후 잔액 정보 반환

balance = 0 # 최초 잔액
balance = deposit(balance,1000) # 1000원 입금
print(balance) # 현재 잔액

# 출금하는 함수
print("----- deposit(출금)테스트 -----")
def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance # 기존 잔액 반환

balance = 0 # 최초 잔액
balance = deposit(balance,1000) # 1000원 입금

# 출금 시도
balance = withdraw(balance,2000) # 2000원 출금 시도 시 잔액이 부족하므로 실패
balance = withdraw(balance,500) # 500원 출금 시도 시 성공
print(balance) # 현재 잔액

# 저녁때 출금(수수료 포함의 경우)
print("----- 저녁때 deposit(출금)테스트 -----")
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 출금 수수료 100원 
    return commission, balance - money - commission # 튜플 형식으로 반환 

balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 튜플은 초기에 공부하였던 배열형이 ()로 감싸져있는 구조였는데,  굳이 ()로 감싸지 않더라도 튜플구조로 사용가능하다.
