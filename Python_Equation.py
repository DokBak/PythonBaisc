#간단한 수식에 대한 공부

print("1+2*3 : ",1+2*3) #7
print("(1+2)*3 : ", (1+2)*3) #9
#계산시 ()를 사용해서 계산 순서를 변경할 수가 있다.

#변수를 계산 해서 출력가능하다.
print("name = (1 + 2) * 4")
name = (1 + 2) * 4 #12
print(name) #12

print("name = name + 12")
name = name + 12
print(name) #24

print("name = name - 12")
name = name - 12
print(name) #12

print("name += 4")
name += 4
print(name) #16

print("name -= 6")
name -= 6
print(name) #10

print("name *= 2")
name *= 2
print(name) #20

print("name /= 5")
name /= 5
print(name) #4.0

print("name **= 2")
name **= 2
print(name) #16.0

print("name //= 3")
name //= 3
print(name) #5.0

print("name %= 4")
name %= 4
print(name) #1.0