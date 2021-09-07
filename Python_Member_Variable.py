# 맴버 변수

# 클래스 내에서 정의된 변수를 맴버변수라고 하며 self. 와 함께 사용할 수 있습니다. Unit 클래스 경우 name, hp, damage가 맴버변수가 된다.

# 객체를 생성 후 객체의 맴버변수를 추가 가능하다.
# 이렇게 객체에 맴버변수를 추가해도, 추가한 객체에만 적용된다.

class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name # 맴버변수 name
        self.hp = hp # 맴버변수 hp
        self.damage = damage # 맴버변수 damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name,wraith1.damage)) # 맴버변수 접근

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)

# 빼앗은 레이스에 클로킹이 업글되어있는 경우, 클로킹 변수를 추가한다.
wraith2.cloaking = True # 빼앗은 레이스만을 위한 특별한 맴버 변수 정의 

if(wraith2.cloaking == True): # 클로킹 상태라면?
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#if(wraith1.cloaking == True): # 클로킹 상태라면?
#    print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))
