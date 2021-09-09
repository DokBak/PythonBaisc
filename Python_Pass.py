# 패스

# Pass는 아무것도 하지 않고 일단은 그냥 넘어간다는 의미로 사용.
# 함수뿐만아니라 if, for, while등에서도 pass를 사용하여 당장의 세부 동작을 정의 하지 않은 채 둿다가 나중에 다시 코드를 완성하도록 할 수 있다.

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

#################### 이전까지의 메서드 일람. ####################

# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알람] 새로운 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()