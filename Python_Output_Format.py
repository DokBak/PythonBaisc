# 다양한 출력포멧

print("-----지금까지 공부하였던 출력 방식-----")
print("{0}".format(500)) # 해당 위치에 500 값을 출력

print("-----공백설정 출력 방식-----")
print("{0: >10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, 10칸 의 공간 확보
# 출력하면 다음과 같이 출력된다. 10칸중 출력할 3칸을 제외한 7칸은 공백으로 남는다.
# 출력문)       500

print("-----부호를 포함한 출력 방식-----")
print("{0: >+10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, 부호기호(+-), 10칸 의 공간 확보
print("{0: >-10}".format(-500))
# 출력문)      +500
# 출력문)      -500

print("-----빈자리 출력설정 포함한 출력 방식-----")
print("{0:_>+10}".format(500)) # 빈 자리는 _로, 좌측 정렬, 부호기호(+-), 10칸 의 공간 확보
print("{0:_>-10}".format(-500))
# 출력문)______+500
# 출력문)______-500

print("-----큰 수 표기시 단위표기용 1,000 콤마 추가 출력 방식-----")
print("{0:,}".format(100000000000)) # 3자리 마다 콤마 찍어주기
print("{0:+,}".format(100000000000)) # 부호기호(+-), 3자리 마다 콤마 찍어주기
print("{0:+,}".format(-100000000000)) # 부호기호(+-), 3자리 마다 콤마 찍어주기
# 출력문)100,000,000,000
# 출력문)+100,000,000,000
# 출력문)-100,000,000,000

print("-----지금까지의 종합-----")
print("{0:^<+30,}".format(100000000000))
# 출력문)+100,000,000,000^^^^^^^^^^^^^^

print("-----소수점출력-----")
print("{0:f}".format(5/3)) # 실수 값 출력
# 출력문)1.666667

print("-----소수점 둘째자리까지 출력-----")
print("{0:.2f}".format(5/3)) # 소수점 둘째자리까지 출력
# 출력문)1.67

print("-----공부내용 요약 정리-----")
print("지금까지 공부한 출력 포멧은 다음과 같은 순서로 {}내에 사용자가 필요한 부분만 명시하는 방식으로 포멧을 정의 할수 있다.")
print("{인덱스 : [[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}")

print("-----모든 옵션 사용한 출력 예제-----")
print("{0}{1:^>+10,.2f},{2:!>+10,.1f}".format("모든옵션 사용 : ",10000/8,20000/7),"     되나?     ",sep="와",end="이랑")
print("   이걸로 복습해보자")