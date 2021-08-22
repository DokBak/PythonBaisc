#세트

# 수학에서 집합과 비슷.
# 중괄호를 이용하여 선언할 수 있다.
# 예시 {value1, value2}
# 중복을 허용하지 않으므로 같은 값은 여러번 적어도 딱 한 번만 들어간다. (자동중복 제거)

my_set = {1,2,3,3,3}
print(my_set) #{1, 2, 3}

# 중괄호{}로 선언하는 방법
# set([값, 값])으로 선언 하는 방법

group1 = {"a", "b", "c"}
group2 = set(["a", "e"])

# 교집합 : 집합의 성질을 이용하여 두 집합 중 공통된 값들만 뽑아내는 교집합은 & 기호나 intersection()을 이용하면 된다.
print("group1 & group2 : ", group1 & group2) # {'a'}
print("group1.intersection(group2) : ", group1.intersection(group2)) # {'a'}

# 합집합 : 두 집합을 합치는 합집합은 키보드의 빅스페이스 근처에 있는 |기호나 union()을 이용하면 된다.
print("group1|group2 : ", group1|group2) # {'a', 'e', 'b', 'c'}
print("group1.union(group2) : ", group1.union(group2)) # {'a', 'e', 'b', 'c'}

# 차집합 : 그룹1에는 있으나 그룹2에는 없는 경우 -기호또는 difference()을 이용하면 된다.
print("group1-group2 : ", group1-group2) # {'c', 'b'}
print("group1.difference(group2) : ",group1.difference(group2)) # {'c', 'b'}
    # 반대의 경우
print("group2-group1 : ", group2-group1) # {'e'}
print("group2.difference(group1) : ",group2.difference(group1)) # {'e'}

# 세트의 데이터 추가 
group1.add("f")
print("group1.add(\"f\") : ", group1) # {'c', 'a', 'f', 'b'}

# 세트의 데이터 제거
group1.remove("b")
print("group1.remove(\"b\") : ", group1) # {'f', 'a', 'c'}