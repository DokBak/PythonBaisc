# 클래스 

# 스타크래프트를 기준으로 생각해보자 
# 테란이란 종족에 마린을 생각해보자

# 유닛의 이름과 체력, 공격력정보를 각각의 변수에 저장하고 유닛이 생성되었다는 내용과 함께 유닛의 정보를 출력하는 것까지 코드를 작성해보자.

# 마린 : 공격 유닛, 군인, 총을 쏠수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{}유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력{1}\n".format(hp,damage))

# 이번엔 탱크유닛을 생성

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력{1}\n".format(tank_hp,tank_damage))


# 위에 생성한 두 유닛을 가지고 공격을 가보자

# 공격 함수
def attack(name, location, damage):
    print("{0}:{1}방향으로 적군을 공격 합니다.[공격력{2}]".format(name,location,damage))

# 1시방향으로 공격을 보낸다 할때 

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 새로운 탱크 유닛 추가
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35


# 추가된 탱크까지 총 3개의 유닛을 공격에 사용해보자 
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank_damage)


# 동일한 내용의 코드를 반복적으로 사용해야할 경우에 클래스를 활용하면 코드를 간소화 시킬수 있다.

# 기본적인 클래스의 구성 : 서로관련있는 변수(맴버변수), 함수(메소드)들의 집합
# class 클래스명:
#   def 메소드1(self, 전달값1, 전달값2,...):
#       실행명령문1
#       실행명령문2
#   def 메소드2(self, 전달값1, 전달값2,...):
#       실행명령문1
#       실행명령문2

class Unit: # 함수와 마찬가지로 정의만으론 아무 동작을 하지 않는다.
    def __init__(self,name, hp,damage):
        self.name = name # 맴버 변수 name에 전달값 name 저장
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# 클래스 통해서 만들어 지는 것을 객체(Object)라고 표현하며, 이 객체는 클래스의 인스턴스(Instance)가 된다.
# Unit클래스를 통해 만들어진 마린과 탱크는 객체라 부름
# 마린과 탱크는 Unit 클래스의 인스턴스라 부름

marine1 = Unit("마린", 40, 5) # 마린1 생성, 전달값으로 name, hp, damage를 전달
marine2 = Unit("마린", 40, 5) # 마린2 생성
tank = Unit("탱크", 150, 35) # 탱크 생성

# 전달값은 클래스의 __init__() 에 정의된 부분중에 self를 제외한 값