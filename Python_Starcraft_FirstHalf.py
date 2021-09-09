# 스타크래프트 프로젝트 전반

# 일반 유닛 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 출력문 추가
    def move(self, location):
        # print("[지상 유닛 이동]") # 출력문 제외
        self.location = location
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    def damaged(self, damage): # AttackUnit에서 Unit으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛 클래스
class AttackUnit(Unit): # 공격 유닛
    def __init__(self, name, hp, speed, damage): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가된 Unit을 정의 
        self.damage = damage
    def attack(self,location): 
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력{2}]".format(self.name,location,self.damage)) 

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10 # 체력 10 감소
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동불가
    siege_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return
        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소 
            self.siege_mode = False # 시즈모드 해제

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)) 

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        # print("[공중 유닛 이동]") # 출력문 제외
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드(해체 상태)
    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaking == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때 
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
        self.cloaked = True