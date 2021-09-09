# 슈퍼

#################### 이전까지의 메서드 일람. ####################

# 일반 유닛 클래스
class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동속도
    def move(self, location): # 이동 함수 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도{2}]".format(self.name, location, self.speed))

# 공격 유닛 클래스
class AttackUnit(Unit): # 공격 유닛
    def __init__(self, name, hp, speed, damage): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가된 Unit을 정의 
        self.damage = damage
    def attack(self,location): # 전달 받은 방향으로 공격
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력{2}]".format(self.name,location,self.damage)) 
    def damaged(self,damage): #damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남ㅇㄴ 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# 공중 유닛 클래스
class Flyable:
    def __init__(self, flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed
    def fly(self, name, location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self, name, hp, 0, damage) # 이름, 체력, 공격력
        Flyable.__init__(self,flying_speed) # 공중 이동 속도
    def move(self, location): # 메소드 오버라이딩을 한다.
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

def game_start():
    print("[알람] 새로운 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()

#################### 이전까지의 메서드 일람. ####################

# 건물
# class BuildingUnit(Unit):
#    def __init__(self,name,hp,location):
#        Unit.__init__(self,name,hp,0) # speed 0 : 건물은 지상 이동 불가
#        self.location = location

# 지금까지는 상속을 받아 부모클래스의 이름을 직접 적고 부모클래스에 접근하였는데 super()를 아용하게 되면 부모클래스의 이름을 직접 작성하지 않아도 된다. 
# 아래의 건물 클래스(BuildingUnit)는 위의 클래스와 동일한 기능을 한다.
# super()를 사용할 때는 self를 제외한다.


# 건물
class BuildingUnit(Unit):
   def __init__(self,name,hp,location):
       super().__init__(name,hp,0) # 부모 클래스 접근. self없이 사용
       self.location = location