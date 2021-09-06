# 퀴즈7

# 당신의 회사에서는 매주 1회 작성해야하는 다음과 같은 보고서가 있습니다. 

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건1 : 파일명은 '1주차.txt', '2주차.txt',...와 같이 만든다.
week = range(1,51)
for oneweek in week:
    with open("{0}주차.txt".format(oneweek),"w",encoding="utf8") as weekfile:
        weekfile.write("- {0: >2}주차 주간보고 -\n".format(oneweek))
        weekfile.write("부서 : \n")
        weekfile.write("이름 : \n")
        weekfile.write("업무 요약 : \n")
