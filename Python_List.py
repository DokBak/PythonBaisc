#리스트

#관련성 있는 변수들을 하나로 묶어서 관리 가능하다.
#타입이 같지 않아도 된다.

bus1 = 101
bus2 = 102
bus3 = 103
print(bus1,bus2,bus3)

# 1. 리스트 선언
bus = [101,102,103]
print(bus) #[101, 102, 103]

subway = ["a","b","c"]
# 2. 해당 항의 인덱스값 추출  #문자열.index(값)
print(subway.index("a")) #0　#"a"의 인덱스값을 추출

# 3. 리스트에 값 추가(제일 후방)  #문자열.append(값)
subway.append("d") # 배열에 추가하는 함수 .append()
print(subway) #["a", "b", "c", "d"]

# 4. 원하는 위치에 값을 추가  #문자열.insert(추가할 위치,값)
subway.insert(1,"e")
print(subway) #["a", "e", "b", "c", "d"]

# 5. 뒤에서 부터 하나씩 제거  #문자열.pop()
subway.pop()
print(subway) #["a", "e", "b", "c"]

subway.pop()
print(subway) #["a", "e", "b"]

subway.pop()
print(subway) #["a", "e"]

# 6. 리스트의 같은 값이 몇 개나 있는지  #문자열.count(값)
subway.append("a")
print(subway) #["a", "e", "a"]
print(subway.count("a")) #2

num_list = [5,2,4,3,1]

# 7. 오름차순으로 정렬 .sort()
num_list.sort()
print(num_list) #[1, 2, 3, 4, 5]

# 8. 내림차순으로 정렬 .reverse()
num_list.reverse()
print(num_list) #[5, 4, 3, 2, 1]

# 9. 리스트 데이터 없애기
num_list.clear()
print(num_list) #[]

# 10. 타입상관없이 작성가능
mix_list = ["k",20,True]
print(mix_list) #["k" ,20, True]

# 11. 리스트를 확장할 수도 있다.
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list) #[5, 2, 4, 3, 1, "k", 20, True]