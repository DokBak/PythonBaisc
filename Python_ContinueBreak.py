# 반복문제어

# 개념 
# Continue : 더 이상 아래 명령들을 실행하지 않고 다음 반복 대상으로 넘어갈때 사용
# Break : 즉시 반복문을 탈출하는데 사용한다.

print("-----countinue 예제-----")
# 예시 10명의 학생들에게 책 읽기를 시킬때, 출석번호 1번부터 10번 까지 총 10명의 학생들이 있고 순서대로 한 문단씩 책으 읽는데 2번과 5번 학생들이 결석을 한 경우
absent = [2,5] # 결석한 학생 출석번호

for student in range(1,11): # range(a,b)  a부터 b전까지
    if student in absent:
        continue
    print("{0}, 책을 읽어봐" .format(student))

# 1 , 책을 읽어봐
# 3, 책을 읽어봐
# 4, 책을 읽어봐
# 6, 책을 읽어봐
# 7, 책을 읽어봐
# 8, 책을 읽어봐
# 9, 책을 읽어봐
# 10, 책을 읽어봐

print("-----break 예제-----")
# 예시 10명의 학생들에게 책 읽기를 시킬때, 출석번호 1번부터 10번 까지 총 10명의 학생들이 있고 순서대로 한 문단씩 책으 읽는데 2번과 5번 학생들이 결석을 한 경우
# 책을 가져오지 않는 학생이 있다면 그대로 수업종료
absent = [2,5] # 결석한 학생 출석번호
no_book = [7] #책을 가져오지 않은 학생 출석번호

for student in range(1,11): # range(a,b)  a부터 b전까지
    if student in absent:
        continue
    elif student in no_book: # 책을 가져오지 않았으면 바로 수업 종료(반복문 탈출)
        print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐" .format(student))

# 1, 책을 읽어봐
# 3, 책을 읽어봐
# 4, 책을 읽어봐
# 6, 책을 읽어봐
# 오늘 수업 여기까지, 7는 교무실로 따라와

