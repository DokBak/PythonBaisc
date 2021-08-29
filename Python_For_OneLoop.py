# 한 줄 for

# 기존의 for문 
# for 변수 in 반복대상
#     실행명령문

# 학생이라는 배열을 있는 그대로 출력한다. 이것을 아래와같이 100을 더하여 출력되도록 작성하면?
students = [1,2,3,4,5]
print(students) #[1,2,3,4,5]

# 기존 for 방식
for oneStudents in students:
    print("{0}".format(oneStudents))

# 1
# 2
# 3
# 4
# 5
# 기존 배열의 있는 항목들을 하나씩 뽑아서 출력해주는 형식으로 사용되어져있다.


# 한 줄 for문의 예시1)
# 정의하고자하는변수명 = [실행명령문 for 집합(배열)에서 한개씩 습득하여 임시저장할 변수명(i) in 가공할변수명]
students = [i+100 for i in students]
print(students) #[101,102,103,104,105]

# 반복대상인 students리스트에서 하나씩 값으 가져와서 i라는 변수에 저장하고, 
# 그 변수를 활용하여 i + 100이라는 명령을 실행한 값드을 새로운 리스트로 만들어서 students에 집어 넣는 의미 



# students = [i+100 for i in students]
# 한 줄 for문의 예의 값을 조금더 풀어서 작성하면 
# students = [students[0] + 100, students[1] + 100, students[2] + 100, students[3] + 100, students[4] + 100]
# 인덱스의 값까지 풀어서 작성하게 되면 
# students = [1+100, 2+100, 3+100, 4+100, 5+100]

# 즉, 기존의 데이터를 가공하여 새로운 데이터로 만들어 준다.
# 배열의 이름 데이터를 가공해서 배열의 이름길이정보로 변환하는 역할을 해준다.


# 한 줄 for문의 예시2)
students = ["Iron man","Thor","I am groot"]
print(students)  #['Iron man', 'Thor', 'I am groot']

students = [len(i) for i in students]
print(students) # [8, 4, 10]

# 한 줄 for문의 예시3)
students = ["Iron man", "Thor", "I am groot"]
print(students) #['Iron man', 'Thor', 'I am groot']

students = [i.upper() for i in students]
print(students) #['IRON MAN', 'THOR', 'I AM GROOT']