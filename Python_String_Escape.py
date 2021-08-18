#탈출문자 

# 줄 바꿈 \n
print("오늘은 너무 너무 피곤하다.")
#이 문장을 두줄로 표현 하고 싶다면 
print("오늘은 너무")
print("너무 피곤하다.")

#이렇게 두줄로 표현도 가능하지만 탈출 문자를 사용하는 편이 좋다.
print("오늘은 너무 \n너무 피곤하다.")

# 따옴표 출력 \" \'
print("이것도 출력 \"가능\" 하려나?")
print("이것도 출력 \"가능\' 하려나?")
#이렇게 탈출문자를 사용할 경우는 "와 ' 동시에 써도 에러가 나지 않는다.

# 역슬래시 출력 \\
# 파일 경로와 같은 문자를 출력하고 싶을 경우 탈출문자의 형태가 있을수 있기때문에 \를 \\로 변경해서 출력해주어야 에러가 발생하지 않는다.

#문자열을 있는 그대로 출력할 때에는 문자열 앞에 r을 입력해주면 파일경로 그대로를 사용가능하다.
print(r"C:\Users\Studying") # C:\User\Studying

# 커서를 맨 앞으로 \r
print("Red Apple\rPine") #PineApple

# 백스페이스 \b
print("Redd\b Apple") #Red Apple

# 탭 \t
print("Red\tApple") # 보통 8칸 단위를 띄워준다 