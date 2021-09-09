# 메소드 오버라이딩

# 상속관계에 있는 클래스들 사이에서 부모 클래스에 정의된 메소드를 그대로 사용하지 않고 자식 클래스에서 같은 이름으로 메소드를 새롭게 정의하여 사용하도록 할 수 있다.

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
        # Unit() 클래스에 있는 move()를 오버라이딩 한다.

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 23, 3)

# 벌쳐와 배틀크루저 이동
vulture.move("1시")
battlecruiser.move("1시")
