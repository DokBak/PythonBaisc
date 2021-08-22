#사전형

# 사전형 자료구조는 마치 자동차 열쇠로는 지정된 차만 여는 것과 같이 딱 한 대의 차만 열수 있도록 되어있다.
# 자바공부시 배웠던 해시맵과 비슷하다.
# key 와 value 쌍으로 이루어져 있다. 

# 구조 : 사전은 중괄호로 둘러싸서 정의할 수 있으며, key와 value는 콜론(:)으로 구분, 두 개 이상의 데이터는 리스트와 마찬가지로 콤마(,)로 구분하면 된다.
# {key1 : value1, key2 : value2}
# 이 때 key들은 중복 값을 허용하지 않는 유일한 값으로 설정해야 한다.

#차 키 번호와 차 번호를 지정
car = {"100":"가2021", "101":"나2021"}

#값을 출력하는것은 변수명[키값]의 형태로 출력가능하다.

print("car[\"100\"] : ", car["100"])
print("car[\"101\"] : ", car["101"])

# 대괄호가 아닌 get()을 이용하는 방법도 있다.

print("car.get(\"100\") : ", car.get("100"))
print("car.get(\"101\") : ", car.get("101"))

#대괄호와 get()방법의 차이는 중간에 프로그램이 종료 여부 차이가 있다.

#print("car[\"111\"] : ", car["111"]) # 뒤의 코드를 실행시키지 않고 그대로 프로그램이 종료된다.
print("car.get(\"111\") : ", car.get("111")) # 사전형에 데이터가 없더라도 None을 출력하며 프로그램은 진행된다. 
print("출력여부를 확인하는 출력문 ") 

# 또한 사전형에서 get()은 기본값을 설정가능하다. 
print("car.get(\"111\") : ", car.get("111", "기본값설정")) # 키 "111"에 value를 설정하기 전까지 이렇게 기본값을 설정하여 출력가능하다.

# key값이 사전 자료형에 정의 되어 있는지 여부를 확인 한다.
print("\"100\" in car : ", "100" in car) # 사전형에 키값이 있다면 True 
print("\"111\" in car : ", "111" in car) # 사전형에 키값이 없다면 False

# 데이터의 업데이트 또는 추가
print("car :", car) # {'100': '가2021', '101': '나2021'}
# key 값이 존재한다면 value 값을 변경
car["100"] = "다2021"
print("car : ", car) # {'100': '다2021', '101': '나2021'}
# key 값이 존재하지 않는 다면 데이터 추가
car["102"] = "라2021"
print("car : ", car) # {'100': '다2021', '101': '나2021', '102': '라2021'}

# 사전형 데이터 삭제 
del car["100"]
print("car : ", car) # {'101': '나2021', '102': '라2021'}

# 현재 사용중인 key값을 전부 출력
print("car.keys() : ", car.keys()) # dict_keys(['101','102'])

# 반대로 사용중인 value값을 전부 출력
print("car.values() : ", car.values()) #dict_value(['나2021','라2021'])

# key, value를 쌍으로 출력 
print("car.items : ",car.items()) # dict_items([('101', '나2021'), ('102', '라2021')])